#!/usr/bin/python

#"usage: 3piece_read_split.py Input_file First_piece_size(bp) Last_piece_size(bp) upstream_to_trim(bp) downstream_to_trim(bp)"
import gzip
import sys
fn1=sys.argv[1]

if 'gz' in fn1:
        dfh1=gzip.open(fn1,'r')

if 'gz' not in fn1:
	dfh1=open(fn1,'r')

ID1=dfh1.readline().split()
line1=dfh1.readline().rstrip()
plus1=dfh1.readline().split()
QS1=dfh1.readline().rstrip()
rfhs=[]


#size1=int(sys.argv[2])
#size2=int(sys.argv[3])
#trim1=int(sys.argv[4])
#trim2=int(sys.argv[5])
size1=40
size2=40
trim1=10
trim2=10

for i in range(1,4):
	rfhs.append(open(fn1+'_r'+str(i)+'.fq','w'))


while line1:
	if len(line1[trim1:size1+trim1])>=30:
		rfhs[0].write(ID1[0].split('_')[0]+'_'+ID1[0].split('_')[1].split(':')[0]+'-1:'+':'.join(ID1[0].split('_')[1].split(':')[1:])+'\n'+line1[trim1:size1+trim1]+'\n'+plus1[0]+'\n'+QS1[trim1:size1+trim1]+'\n')
	if len(line1[trim1+size1:(-1*size2)-trim2])>=30:
		rfhs[1].write(ID1[0].split('_')[0]+'_'+ID1[0].split('_')[1].split(':')[0]+'-2:'+':'.join(ID1[0].split('_')[1].split(':')[1:])+'\n'+line1[trim1+size1:(-1*size2)-trim2]+'\n'+plus1[0]+'\n'+QS1[trim1+size1:(-1*size2)-trim2]+'\n')
	if len(line1[(-1*size2)-trim2:])>=30:
		rfhs[2].write(ID1[0].split('_')[0]+'_'+ID1[0].split('_')[1].split(':')[0]+'-3:'+':'.join(ID1[0].split('_')[1].split(':')[1:])+'\n'+line1[(-1*size2)-trim2:]+'\n'+plus1[0]+'\n'+QS1[(-1*size2)-trim2:]+'\n')
	ID1=dfh1.readline().split()
	line1=dfh1.readline().rstrip()
	plus1=dfh1.readline().split()
	QS1=dfh1.readline().rstrip()

map(lambda x:x.close(),rfhs)
