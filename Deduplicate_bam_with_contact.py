import pysam  
import sys
import os
os.system('sort -k1n '+sys.argv[1]+'_multi_split_aligned.txt_man_dedupped.txt > '+sys.argv[1]+'_multi_split_aligned.txt_man_dedupped_queryname_sorted.txt')
bam=sys.argv[1]
dfh=pysam.AlignmentFile(bam, "rb")
dfh2=open(sys.argv[1]+'_multi_split_aligned.txt_man_dedupped_queryname_sorted.txt','r')
rfh=pysam.AlignmentFile(sys.argv[1].replace('.bam','_dedupped.bam'), "wb", template=dfh)
dfh2.readline()
read='a a'
count=0
for i in dfh2:
	line=i.split()
	qq=0
	if read[0].split('_')[0]==line[1]:
		qq+=1
	for a in dfh:
		read=str(a).split()
		if read[0].split('_')[0]==line[1]:
			rfh.write(a)
			qq+=1
		if read[0].split('_')[0]!=line[1] and qq!=0:
			break
	if qq==0:
		print ("Something is wrong. Please contact eaststar0@gmail.com")
		break
	if qq!=0:
		count+=1
