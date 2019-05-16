#!/usr/bin/env python

import os
import sys
com=sys.argv
if '-r' not in com or '-1' not in com or "-2" not in com:
	print "USAGE: python TAURUS-MH -r <genome_folder> -1 <G to A converted mate> -2 <C to T converted mate> -Trim1 <Trim off first Xbp of reads> -Trim2 <Trim off last Xbp of reads> -split1 <Use first Xbp of unmapped read for 1st split reads> -split3 <Use last Xbp of unmapped read for 3rd split reads>"

REF=sys.argv[com.index('-r')+1]
R1_pre=sys.argv[com.index('-1')+1]
R2_pre=sys.argv[com.index('-2')+1]
if '-Trim1' in com:
	T1=sys.argv[com.index('-Trim1')+1]
if '-Trim1' not in com:
	T1='25'
if '-Trim2' in com:
	T2=sys.argv[com.index('-Trim2')+1]
if '-Trim2' not in com:
	T2='3'
if '-split1' in com:
	S1=sys.argv[com.index('-split1')+1]
if '-split1' not in com:
	S1='40'
if '-split2' in com:
	S2=sys.argv[com.index('-split2')+1]
if '-split2' not in com:
	S2='40'

R1=R1_pre.split('/')[-1]+'_trimmed.fastq'
R2=R2_pre.split('/')[-1]+'_trimmed.fastq'

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
+"\nR1_pre="+R1_pre\
+"\nR2_pre="+R2_pre\
+"\nR1="+R1\
+"\nR2="+R2\
+"\nR1_mod="+R1_mod\
+"\nR2_mod="+R2_mod\
+"\n"
+"\n${python}/python ${TAURUS_loc}/Trimming.py ${R1_pre} "+T1+" "+T2+" &"\
+"\nwait"\
+"\n"
+"\n${bismark}/bismark --bowtie1 --path_to_bowtie ${bowtie} -un ${REF} ${R2} & "
+"\n${bismark}/bismark --bowtie1 --path_to_bowtie ${bowtie} -un --pbat ${REF} ${R1} &"
+"\nwait"\
+"\n"\
+"\n${python}/python ${TAURUS_loc}/3piece_read_split.py ${R1}_unmapped_reads.fq.gz "+S1+" "+S2+" &"\
+"\n${python}/python ${TAURUS_loc}/3piece_read_split.py ${R2}_unmapped_reads.fq.gz "+S1+" "+S2+" &"\
+"\nwait"\
+"\n${bismark}/bismark --bowtie1 --path_to_bowtie ${bowtie} --pbat ${REF} ${R1}_unmapped_reads.fq.gz_r1.fq &"\
+"\n${bismark}/bismark --bowtie1 --path_to_bowtie ${bowtie} ${REF} ${R2}_unmapped_reads.fq.gz_r1.fq &"\
+"\nwait"\
+"\n"
+"\n${bismark}/deduplicate_bismark --bam --output_dir ./ \\"
+"\n${R1_mod}_bismark.bam \\"
+"\n${R2_mod}_bismark.bam \\"
+"\n${R1}_unmapped_reads.fq.gz_r1_bismark.bam \\" 
+"\n${R2}_unmapped_reads.fq.gz_r1_bismark.bam \\" 
+"\n"
+"\njava -jar -Xmx10g ${picard}/picard.jar MergeSamFiles SO=queryname \\"
+"\nI=${R1_mod}_bismark.bam \\"
+"\nI=${R2_mod}_bismark.bam \\"
+"\nI=${R1}_unmapped_reads.fq.gz_r1_bismark.bam \\"
+"\nI=${R2}_unmapped_reads.fq.gz_r1_bismark.bam \\"
+"\nO=${R1}_all_merged_3split.bam "\
+"\n"
+"\n${python}/python ${TAURUS_loc}/Bam_to_multi_contact.py ${R1}_all_merged_3split.bam"\
+"\n${python}/python ${TAURUS_loc}/Deduplicate_multi_contact.py ${R1}_all_merged_3split.bam_multi_split_aligned.txt"\
+"\n${python}/python ${TAURUS_loc}/Multi_contact_to_two_contact_stat_no_less.py ${R1}_all_merged_3split.bam_multi_split_aligned.txt"
+"\n${python}/python ${TAURUS_loc}/Stat_summary.py ${R1_pre}")

rfh.close()
os.system("sh Run_TAURUS-MH_"+R1.split("/")[-1]+".sh")
