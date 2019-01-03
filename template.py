#!/usr/bin/env python

import os
import sys
print "USAGE: python TAURUS-MH <genome_folder> <G to A converted mate> <C to T converted mate>"

REF=sys.argv[1]
R1=sys.argv[2]
R2=sys.argv[3]

if 'gz' in R1.split('.')[-1]:
	R1_mod='.'.join(R1.split('.')[:-2]).split('/')[-1]
if 'gz' not in R1.split('.')[-1]:
	R1_mod='.'.join(R1.split('.')[:-1]).split('/')[-1]
if 'gz' in R2.split('.')[-1]:
        R2_mod='.'.join(R2.split('.')[:-2]).split('/')[-1]
if 'gz' not in R2.split('.')[-1]:
        R2_mod='.'.join(R2.split('.')[:-1]).split('/')[-1]

rfh=open('Run_TAURUS-MH_'+R1.split('/')[-1]+'.sh','w')

rfh.write("bismark="+bismark\
+"\nbowtie="+bowtie\
+"\npicard="+picard\
+"\nTAURUS_loc="+TAURUS_loc\
+"\npython="+python\
+"\nREF="+REF\
+"\nR1="+R1\
+"\nR2="+R2\
+"\nR1_mod="+R1_mod\
+"\nR2_mod="+R2_mod\
+"\n"
+"\n${python}/python ${TAURUS_loc}/Trimming.py ${R1_pre} &"\
+"\n${python}/python ${TAURUS_loc}/Trimming.py ${R2_pre} &"\
+"\nwait"\
+"\n"
+"\n${bismark}/bismark --bowtie1 --path_to_bowtie ${bowtie} -un ${REF} ${R2} & "
+"\n${bismark}/bismark --bowtie1 --path_to_bowtie ${bowtie} -un --pbat ${REF} ${R1} &"
+"\nwait"\
+"\n"\
+"\nR1="+R1.split('/')[-1]\
+"\nR2="+R2.split('/')[-1]\
+"\n${python}/python ${TAURUS_loc}/3piece_read_split.py ${R1}_unmapped_reads.fq.gz &"\
+"\n${python}/python ${TAURUS_loc}/3piece_read_split.py ${R2}_unmapped_reads.fq.gz &"\
+"\nwait"\
+"\n${bismark}/bismark --bowtie1 --path_to_bowtie ${bowtie} --pbat ${REF} ${R1}_unmapped_reads.fq.gz_r1.fq ${R1}_unmapped_reads.fq.gz_r2.fq ${R1}_unmapped_reads.fq.gz_r3.fq &"\
+"\n${bismark}/bismark --bowtie1 --path_to_bowtie ${bowtie} ${REF} ${R2}_unmapped_reads.fq.gz_r1.fq ${R2}_unmapped_reads.fq.gz_r2.fq ${R2}_unmapped_reads.fq.gz_r3.fq &"\
+"\nwait"\
+"\n"
+"\n${bismark}/deduplicate_bismark --bam --output_dir ./ \\"
+"\n${R1_mod}_bismark.bam \\"
+"\n${R2_mod}_bismark.bam \\"
+"\n${R1}_unmapped_reads.fq.gz_r1_bismark.bam \\" 
+"\n${R1}_unmapped_reads.fq.gz_r2_bismark.bam \\"
+"\n${R1}_unmapped_reads.fq.gz_r3_bismark.bam \\" 
+"\n${R2}_unmapped_reads.fq.gz_r1_bismark.bam \\" 
+"\n${R2}_unmapped_reads.fq.gz_r2_bismark.bam \\" 
+"\n${R2}_unmapped_reads.fq.gz_r3_bismark.bam "\
+"\n"
+"\njava -jar -Xmx10g ${picard}/picard.jar MergeSamFiles SO=queryname \\"
+"\nI=${R1_mod}_bismark.bam \\"
+"\nI=${R2_mod}_bismark.bam \\"
+"\nI=${R1}_unmapped_reads.fq.gz_r2_bismark.bam \\"
+"\nI=${R1}_unmapped_reads.fq.gz_r3_bismark.bam \\"
+"\nI=${R1}_unmapped_reads.fq.gz_r1_bismark.bam \\"
+"\nI=${R1}_unmapped_reads.fq.gz_r2_bismark.bam \\"
+"\nI=${R1}_unmapped_reads.fq.gz_r3_bismark.bam \\"
+"\nO=${R1}_all_merged_3split.bam "\
+"\n"
+"\n${python}/python ${TAURUS_loc}/Bam_to_multi_contact.py ${R1}_all_merged_3split.bam"\
+"\n${python}/python ${TAURUS_loc}/Deduplicate_multi_contact.py ${R1}_all_merged_3split.bam_multi_split_aligned.txt"\
+"\n${python}/python ${TAURUS_loc}/Multi_contact_to_two_contact_stat.py  ${R1}_all_merged_3split.bam_multi_split_aligned.txt")

rfh.close()
os.system("sh Run_TAURUS-MH_"+R1.split("/")[-1]+".sh")
