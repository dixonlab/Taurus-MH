import sys
fn=sys.argv[1]
dfh=open(fn,'r')
dfh.readline()
rfh=open(fn+'_man_dedupped.txt','w')
stat=open(fn+'_Aligned_Fragment_count.txt','w')
pre=''
duplicate=0
total=0
First_aligned=0
Second_aligned=0
Used_Frag=0

for i in dfh:
	line=i.split()
	total+=1
#	if line[1]!='na':
#		First_aligned+=1
#	if line[-1]!='na':
#		First_aligned+=1
#	for a in line[2:-1]:
#		if a!='na':
#			Second_aligned+=1
	if line[1:]!=pre[1:]:
		rfh.write(i)
		pre=line
#	elif line[1:]==pre[1:]:
#		duplicate+=1
	if 8-line.count('na')>=2:
		Used_Frag+=1
#print fn.split('/')[-1]+'\tDededuplication_stat: Total_Fragment 1st_alignement_mapped 2nd_alignment_mapped Removed_duplicates(%), Remain_Fragments(%) Used_for_contact(%): '+str(total)+'\t'+str(First_aligned)+'\t'+str(Second_aligned)+'\t'+str(duplicate)+' ('+str(round(100*float(duplicate)/total,2))+'%)'+'\t'+str(total-duplicate)+' ('+str(100-(round(100*float(duplicate)/total,2)))+'%)'+'\t'+str(Used_Frag)+' ('+str(round(100*float(Used_Frag)/(float(total-duplicate)),2))+'%)'
stat.write(fn.split('/')[-1]+'\t'+str(Used_Frag)+'\n')
rfh.close()
