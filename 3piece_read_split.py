#!/usr/bin/python

#"usage: 3piece_read_split.py Input_file First_piece_size(bp) Last_piece_size(bp) upstream_to_trim(bp) downstream_to_trim(bp)"
import gzip
import sys
fn1=sys.argv[1]

if 'gz' in fn1:
        dfh1=gzip.open(fn1,'r')

if 'gz' not in fn1:
	dfh1=open(fn1,'r')
if sys.version_info[0]==3:
	ID1=str(dfh1.readline().rstrip())[2:-1]
	line1=str(dfh1.readline().rstrip())[2:-1]
	plus1=str(dfh1.readline().rstrip())[2:-1]
	QS1=str(dfh1.readline().rstrip())[2:-1]
if sys.version_info[0]==2:
	ID1=dfh1.readline().rstrip()
	line1=dfh1.readline().rstrip()
	plus1=dfh1.readline().rstrip()
	QS1=dfh1.readline().rstrip()
rfhs=[]

size1=int(sys.argv[2])
size2=int(sys.argv[3])
trim1=5
trim2=5

for i in range(1,4):
	rfhs.append(open(fn1+'_r'+str(i)+'.fq','w'))


while line1:
	if len(line1[trim1:size1+trim1])>=30:
		rfhs[0].write(str(ID1)+'-1'+'\n'+str(line1[trim1:size1+trim1])+'\n'+str(plus1[0])+'\n'+str(QS1[trim1:size1+trim1])+'\n')
	if len(line1[trim1+size1:(-1*size2)-trim2])>=30:
		rfhs[0].write(str(ID1)+'-2'+'\n'+str(line1[trim1+size1:(-1*size2)-trim2])+'\n'+str(plus1[0])+'\n'+str(QS1[trim1+size1:(-1*size2)-trim2])+'\n')
	if len(line1[(-1*size2)-trim2:-1*trim2])>=30:
		rfhs[0].write(str(ID1)+'-3'+'\n'+str(line1[(-1*size2)-trim2:-1*trim2])+'\n'+str(plus1[0])+'\n'+str(QS1[(-1*size2)-trim2:-1*trim2])+'\n')
	if sys.version_info[0]==3:
		ID1=str(dfh1.readline().rstrip())[2:-1]
		line1=str(dfh1.readline().rstrip())[2:-1]
		plus1=str(dfh1.readline().rstrip())[2:-1]
		QS1=str(dfh1.readline().rstrip())[2:-1]

map(lambda x:x.close(),rfhs)
