import sys
import gzip
dfh1=gzip.open(sys.argv[1],'r')
dfh2=gzip.open(sys.argv[1].replace('R1','R2'),'r')
rfh1=open(sys.argv[1].split('/')[-1]+'_F25_L3_trimmed.fastq','w')
rfh2=open(sys.argv[1].split('/')[-1].replace('R1','R2')+'_F25_L3_trimmed.fastq','w')
line1_1=dfh1.readline()
line1_2=dfh1.readline()
line1_3=dfh1.readline()
line1_4=dfh1.readline()

line2_1=dfh2.readline()
line2_2=dfh2.readline()
line2_3=dfh2.readline()
line2_4=dfh2.readline()
while line1_1:
        if len(line1_2[25:-4])>=20 and line2_2[25:-4]>=20:
                rfh1.write(line1_1+line1_2[25:-4]+'\n'+line1_3+line1_4[25:-4]+'\n')
                rfh2.write(line2_1+line2_2[25:-4]+'\n'+line2_3+line2_4[25:-4]+'\n')
        line1_1=dfh1.readline()
        line1_2=dfh1.readline()
        line1_3=dfh1.readline()
        line1_4=dfh1.readline()
        line2_1=dfh2.readline()
        line2_2=dfh2.readline()
        line2_3=dfh2.readline()
        line2_4=dfh2.readline()
if len(line1_2[25:-4])>=20 and line2_2[25:-4]>=20:                                  
        rfh1.write(line1_1+line1_2[25:-4]+'\n'+line1_3+line1_4[25:-4]+'\n')
        rfh2.write(line2_1+line2_2[25:-4]+'\n'+line2_3+line2_4[25:-4]+'\n')
rfh1.close()
dfh1.close()
rfh2.close()
dfh2.close()
