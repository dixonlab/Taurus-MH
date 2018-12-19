import pysam
import sys
fn=sys.argv[1]
rfh=open(fn.split('/')[-1]+'_multi_split_aligned_temp.txt','w')

IDs=[]
align=[]
splits=['1','1-1','1-2','1-3','2-3','2-2','2-1','2']
count=0

rfh.write('ID\t'+'\t'.join(splits)+'\n')
dfh=pysam.AlignmentFile(fn, "rb")

pre_ID=''

count=0
locs=[]

for i in splits:
        locs.append('na')

for read in dfh:
        line=str(read).split()
        if '_' in line[0]:
                ID=line[0].split('_')[0]                                                                  
                split_st=line[0].split('_')[1].split(':')[0]
                if ID!=pre_ID:
                        if pre_ID!='':
                                rfh.write(pre_ID+'\t'+'\t'.join(locs)+'\n')
                        pre_ID=ID
                        locs=[]
                        for i in splits:
                                locs.append('na')
                locs[splits.index(split_st)]=dfh.get_reference_name(read.reference_id)+':'+str(read.pos+1)
rfh.write(pre_ID+'\t'+'\t'.join(locs)+'\n')
rfh.close()
import os
os.system('sort -k2 '+fn.split('/')[-1]+'_multi_split_aligned_temp.txt > '+fn.split('/')[-1]+'_multi_split_aligned.txt')
os.system('rm '+fn.split('/')[-1]+'_multi_split_aligned_temp.txt')
