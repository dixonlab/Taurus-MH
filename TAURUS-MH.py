#!/usr/bin/env python

import os
import sys
print "USAGE: TAURUS-MH <path_to_bismark_folder> <path_to_bowtie1> <genome_folder> {-1 <mates1> -2 <mates2>}"

bismark=sys.argv[1]
bowtie=sys.argv[2]
REF=sys.argv[3]
R1=sys.argv[4]
R2=sys.argv[5]

if 'gz' in R1.split('.')[-1]:
        R1_mod='.'.join(R1.split('.')[:-2]).split('/')[-1]
if 'gz' not in R1.split('.')[-1]:
        R1_mod='.'.join(R1.split('.')[:-1]).split('/')[-1]
if 'gz' in R2.split('.')[-1]:
        R2_mod='.'.join(R2.split('.')[:-2]).split('/')[-1]
if 'gz' not in R2.split('.')[-1]:
        R2_mod='.'.join(R2.split('.')[:-1]).split('/')[-1]

os.system(bismark+"/bismark --bowtie1 --path_to_bowtie "+bowtie+" -un "+REF+" "+R2+" &&"\
        +bismark+"/bismark --bowtie1 --path_to_bowtie "+bowtie+" -un --pbat "+REF+" "+R1)

R1=R1.split('/')[-1]
R2=R2.split('/')[-1]

os.system("python ./3piece_read_split.py "+R1+"_unmapped_reads.fq.gz &&\
        python ./3piece_read_split.py "+R2+"_unmapped_reads.fq.gz &&"\
+bismark+"/bismark --bowtie1 --path_to_bowtie "+bowtie+" --pbat "+REF+' '+R1+'_unmapped_reads.fq.gz_r1.fq '+R1+'_unmapped_reads.fq.gz_r2.fq '+R1+'_unmapped_reads.fq.gz_r3.fq &&'\
+bismark+"/bismark --bowtie1 --path_to_bowtie "+bowtie+" "+REF+' '+R2+'_unmapped_reads.fq.gz_r1.fq '+R2+'_unmapped_reads.fq.gz_r2.fq '+R2+'_unmapped_reads.fq.gz_r3.fq &&'\
+bismark+"/deduplicate_bismark --bam --output_dir ./ \
"+R1_mod+"_bismark.bam \
"+R2_mod+"_bismark.bam \
"+R1+"_unmapped_reads.fq.gz_r1_bismark.bam \
"+R1+"_unmapped_reads.fq.gz_r2_bismark.bam \
"+R1+"_unmapped_reads.fq.gz_r3_bismark.bam \
"+R2+"_unmapped_reads.fq.gz_r1_bismark.bam \
"+R2+"_unmapped_reads.fq.gz_r2_bismark.bam \
"+R2+"_unmapped_reads.fq.gz_r3_bismark.bam &&"\
+"java -jar -Xmx10g '+picard+' MergeSamFiles SO=queryname \
I="+R1_mod+"_bismark.bam \
I="+R2_mod+"_bismark.bam \
I="+R1+"_unmapped_reads.fq.gz_r2_bismark.bam \
I="+R1+"_unmapped_reads.fq.gz_r3_bismark.bam \
I="+R1+"_unmapped_reads.fq.gz_r1_bismark.bam \
I="+R1+"_unmapped_reads.fq.gz_r2_bismark.bam \
I="+R1+"_unmapped_reads.fq.gz_r3_bismark.bam \
O="+R1+"_all_merged_3split.bam && "\
+"./Bam_to_multi_contact.py "+R1+"_all_merged_3split.bam && "\
+"./Deduplicate_multi_contact.py "+R1+"_all_merged_3split.bam_multi_split_aligned.txt && "\
+"./Multi_contact_to_two_contact_stat.py "+R1+"_all_merged_3split.bam_multi_split_aligned.txt")
