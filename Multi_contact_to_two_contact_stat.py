import sys
fn=sys.argv[1]
dfh=open(fn,'r')
rfh=open('./'+fn.split('/')[-1]+'_2_contacts.txt','w')
stat_rfh=open('./'+fn.split('/')[-1]+'_2_contacts.stats.txt','w')

dfh.readline()
def foo(x, y):
    return 0 if y == 0 else x / y


non_split_all=0
non_split_mapped_both=0
non_split_mapped_only=0
non_split_match=0
Total_Aligned_read=0
intra_less=0
intra_more=0
inter=0
no_split_intra_less=0
no_split_intra_more=0
no_split_inter=0

for i in dfh:
	line=i.split()
	all_data=line[1:]
	Total_Aligned_read+=(8-all_data.count('na'))
	if 8-all_data.count('na')>=2:
		for a in range(0,8):
			if all_data[a]!='na':
				read1=all_data[a]
				break
		for b in range(1,8-a):
			if all_data[-1*b]!='na':
				read2=all_data[-1*b]
				read1_chro=read1.split(':')[0]
				read1_pos=int(read1.split(':')[1])
				read2_chro=read2.split(':')[0]
				read2_pos=int(read2.split(':')[1])
				rfh.write(read1_chro+'\t'+str(read1_pos)+'\t'+read2_chro+'\t'+str(read2_pos)+'\n')
				if read1_chro==read2_chro:
					if abs(read1_pos-read2_pos)<1000:
						intra_less+=1
						if line[1]!='na' and line[-1]!='na':
							no_split_intra_less+=1
					elif abs(read1_pos-read2_pos)>=1000:
						intra_more+=1
						if line[1]!='na' and line[-1]!='na':
							no_split_intra_more+=1
				if read1_chro!=read2_chro:
					inter+=1
					if line[1]!='na' and line[-1]!='na':
						no_split_inter+=1
				break
intra_more=float(intra_more)
intra_less=float(intra_less)
inter=float(inter)
print fn+'\t'+'Total_mapped_Fragment, Total_Mapped_Read_pair, Intra_less, Intra_more, Inter: '+str(Total_Aligned_read)+'\t'+str(intra_less+intra_more+inter)+'\t'+str(intra_less)+' ('+str(round(100*foo(intra_less,(intra_less+intra_more+inter)),2))+'%)'+'\t'+str(intra_more)+' ('+str(round(100*foo(intra_more,(intra_less+intra_more+inter)),2))+'%)'+'\t'+str(inter)+' ('+str(round(100*foo(inter,(intra_less+intra_more+inter)),2))+'%)'
print fn+'\t'+'No_split_stat: Total_mapped_Fragment, Total_Mapped_Read_pair, Intra_less, Intra_more, Inter: '+'\t'+str(Total_Aligned_read)+'\t'+str(no_split_intra_less+no_split_intra_more+no_split_inter)+'\t'+str(no_split_intra_less)+' ('+str(round(100*foo(no_split_intra_less,(no_split_intra_less+no_split_intra_more+no_split_inter)),2))+'%)'+'\t'+str(no_split_intra_more)+' ('+str(round(100*foo(no_split_intra_more,(no_split_intra_less+no_split_intra_more+no_split_inter)),2))+'%)'+'\t'+str(no_split_inter)+' ('+str(round(100*foo(no_split_inter,(no_split_intra_less+no_split_intra_more+no_split_inter)),2))+'%)'

stat_rfh.write(fn+'\t'+'Total_mapped_Fragment, Total_Mapped_Read_pair, Intra_less, Intra_more, Inter: '+str(Total_Aligned_read)+'\t'+str(intra_less+intra_more+inter)+'\t'+str(intra_less)+' ('+str(round(100*foo(intra_less,(intra_less+intra_more+inter)),2))+'%)'+'\t'+str(intra_more)+' ('+str(round(100*foo(intra_more,(intra_less+intra_more+inter)),2))+'%)'+'\t'+str(inter)+' ('+str(round(100*foo(inter,(intra_less+intra_more+inter)),2))+'%)\n')
stat_rfh.write(fn+'\t'+'No_split_stat: Total_mapped_Fragment, Total_Mapped_Read_pair, Intra_less, Intra_more, Inter'+'\t'+str(Total_Aligned_read)+'\t'+str(no_split_intra_less+no_split_intra_more+no_split_inter)+'\t'+str(no_split_intra_less)+' ('+str(round(100*foo(no_split_intra_less,(no_split_intra_less+no_split_intra_more+no_split_inter)),2))+'%)'+'\t'+str(no_split_intra_more)+' ('+str(round(100*foo(no_split_intra_more,(no_split_intra_less+no_split_intra_more+no_split_inter)),2))+'%)'+'\t'+str(no_split_inter)+' ('+str(round(100*foo(no_split_inter,(no_split_intra_less+no_split_intra_more+no_split_inter)),2))+'%)')
