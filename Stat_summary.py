import sys
ref=[sys.argv[1]]
rfh=open(sys.argv[1]+'_summary.txt','w')
rfh.write('Sample\tSequenced_Read-pair\tMapped_Read-pair\tNonclonal_Read-pair\tIntra_less\tIntra_less\tInter\tCpG_met\tCHG_met\tCHH_met\n')
for fn in ref:
        fn=fn.split()[-1].split('/')[-1]
        dfh1=open(fn+'_trimmed_bismark_SE_report.txt','r')
        dfh2=open(fn+'_trimmed.fastq_all_merged_3split.bam_multi_split_aligned.txt_Mapped_Read_count.txt','r')
        dfh3=open(fn+'_trimmed.fastq_all_merged_3split.bam_multi_split_aligned.txt_2_contacts.stats.txt','r')
        data=[0,0,0,0,0,0,0,0,0,0]
        for i in dfh1:
                line=i.split()
                if 'Sequences analysed in total:' in i:
                        data[0]=line[-1]
                if 'Number of alignments with a unique best hit from the different alignments:' in i:
                        data[1]=line[-1]
                if 'C methylated in CpG context:' in i:
                        data[-3]=line[-1]
                if 'C methylated in CHG context:' in i:
                        data[-2]=line[-1]
                if 'C methylated in CHH context:' in i:
                        data[-1]=line[-1]
        line=dfh2.readline().split()
        data[2]=line[-1]
        line=dfh3.readline().split()
        data[3]=line[-7]
        data[4]=line[-6]+' '+line[-5]
        data[5]=line[-4]+' '+line[-3]
        data[6]=line[-2]+' '+line[-1]
        rfh.write(fn+'\t'+'\t'.join(map(lambda x:str(x),data))+'\n')
