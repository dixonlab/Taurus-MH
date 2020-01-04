import sys
import gzip
if '.gz' in sys.argv[1]:
	dfh1=gzip.open(sys.argv[1],'r')
	dfh2=gzip.open(sys.argv[1].replace('R1','R2'),'r')
if '.gz' not in sys.argv[1]:
	dfh1=open(sys.argv[1],'r')
	dfh2=open(sys.argv[1].replace('R1','R2'),'r')
rfh1=open(sys.argv[1].split('/')[-1]+'_trimmed.fastq','w')
rfh2=open(sys.argv[1].split('/')[-1].replace('R1','R2')+'_trimmed.fastq','w')
F_trim=int(sys.argv[2])
B_trim=int(sys.argv[3])

if '.gz' not in sys.argv[1]:
	line1_1=dfh1.readline().rstrip()
	line1_2=dfh1.readline().rstrip()
	line1_3=dfh1.readline().rstrip()
	line1_4=dfh1.readline().rstrip()
	line2_1=dfh2.readline().rstrip()
	line2_2=dfh2.readline().rstrip()
	line2_3=dfh2.readline().rstrip()
	line2_4=dfh2.readline().rstrip()
if '.gz' in sys.argv[1]:
	line1_1=str(dfh1.readline())[2:-3]
	line1_2=str(dfh1.readline())[2:-3]
	line1_3=str(dfh1.readline())[2:-3]
	line1_4=str(dfh1.readline())[2:-3]
	line2_1=str(dfh2.readline())[2:-3]
	line2_2=str(dfh2.readline())[2:-3]
	line2_3=str(dfh2.readline())[2:-3]
	line2_4=str(dfh2.readline())[2:-3]

print (line1_1)
print (line1_2)
print (line1_3)
print (line1_4)
exit()

while line1_1:
	if B_trim!=0:
		if len(line1_2[F_trim:-1*B_trim])>=25 and len(line2_2[F_trim:-1*B_trim])>=25:
			rfh1.write(line1_1.rstrip()+'_1\n'+line1_2[F_trim:-1*B_trim]+'\n'+line1_3+line1_4[F_trim:-1*B_trim]+'\n')
			rfh2.write(line2_1.rstrip()+'_2\n'+line2_2[F_trim:-1*B_trim]+'\n'+line2_3+line2_4[F_trim:-1*B_trim]+'\n')
	if B_trim==0:
		if len(line1_2[F_trim:])>=25 and len(line2_2[F_trim:])>=25:
			rfh1.write(line1_1.rstrip()+'_1\n'+line1_2[F_trim:]+'\n'+line1_3+line1_4[F_trim:]+'\n')
			rfh2.write(line2_1.rstrip()+'_2\n'+line2_2[F_trim:]+'\n'+line2_3+line2_4[F_trim:]+'\n')
	if '.gz' not in sys.argv[1]:
		line1_1=dfh1.readline()
		line1_2=dfh1.readline()
		line1_3=dfh1.readline()
		line1_4=dfh1.readline()
		line2_1=dfh2.readline()
		line2_2=dfh2.readline()
		line2_3=dfh2.readline()
		line2_4=dfh2.readline()
	if '.gz' in sys.argv[1]:
		line1_1=str(dfh1.readline())[2:-3]
		line1_2=str(dfh1.readline())[2:-3]
		line1_3=str(dfh1.readline())[2:-3]
		line1_4=str(dfh1.readline())[2:-3]
		line2_1=str(dfh2.readline())[2:-3]
		line2_2=str(dfh2.readline())[2:-3]
		line2_3=str(dfh2.readline())[2:-3]
		line2_4=str(dfh2.readline())[2:-3]
if B_trim!=0:
        if len(line1_2[F_trim:-1*B_trim])>=25 and len(line2_2[F_trim:-1*B_trim])>=25:
                rfh1.write(line1_1.rstrip()+'_1\n'+line1_2[F_trim:-1*B_trim]+'\n'+line1_3+line1_4[F_trim:-1*B_trim]+'\n')
                rfh2.write(line2_1.rstrip()+'_2\n'+line2_2[F_trim:-1*B_trim]+'\n'+line2_3+line2_4[F_trim:-1*B_trim]+'\n')
if B_trim==0:
        if len(line1_2[F_trim:])>=25 and len(line2_2[F_trim:])>=25:
                rfh1.write(line1_1.rstrip()+'_1\n'+line1_2[F_trim:]+'\n'+line1_3+line1_4[F_trim:]+'\n')
                rfh2.write(line2_1.rstrip()+'_2\n'+line2_2[F_trim:]+'\n'+line2_3+line2_4[F_trim:]+'\n')
rfh1.close()
dfh1.close()
rfh2.close()
dfh2.close()
