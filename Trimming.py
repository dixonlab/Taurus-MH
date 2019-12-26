import sys
import gzip
dfh1=gzip.open(sys.argv[1],'r')
dfh2=gzip.open(sys.argv[1].replace('R1','R2'),'r')
rfh1=open(sys.argv[1].split('/')[-1]+'_trimmed.fastq','w')
rfh2=open(sys.argv[1].split('/')[-1].replace('R1','R2')+'_trimmed.fastq','w')
F_trim=int(sys.argv[2])
B_trim=int(sys.argv[3])
line1_1=dfh1.readline()
line1_2=dfh1.readline()
line1_3=dfh1.readline()
line1_4=dfh1.readline()

line2_1=dfh2.readline()
line2_2=dfh2.readline()
line2_3=dfh2.readline()
line2_4=dfh2.readline()

while line1_1:
        if B_trim!=0:
                if len(line1_2[F_trim:-1*B_trim])>=50 and line2_2[F_trim:-1*B_trim]>=50:
                        rfh1.write(line1_1+line1_2[F_trim:-1*B_trim]+'\n'+line1_3+line1_4[F_trim:-1*B_trim]+'\n')
                        rfh2.write(line2_1+line2_2[F_trim:-1*B_trim]+'\n'+line2_3+line2_4[F_trim:-1*B_trim]+'\n')
        if B_trim==0:
                if len(line1_2[F_trim:])>=50 and line2_2[F_trim:]>=50:
                        rfh1.write(line1_1+line1_2[F_trim:]+'\n'+line1_3+line1_4[F_trim:]+'\n')
                        rfh2.write(line2_1+line2_2[F_trim:]+'\n'+line2_3+line2_4[F_trim:]+'\n')
        line1_1=dfh1.readline()
        line1_2=dfh1.readline()
        line1_3=dfh1.readline()
        line1_4=dfh1.readline()
        line2_1=dfh2.readline()
        line2_2=dfh2.readline()
        line2_3=dfh2.readline()
        line2_4=dfh2.readline()
if B_trim!=0:
        if len(line1_2[F_trim:-1*B_trim])>=50 and line2_2[F_trim:-1*B_trim]>=50:                                  
                rfh1.write(line1_1+line1_2[F_trim:-1*B_trim]+'\n'+line1_3+line1_4[F_trim:-1*B_trim]+'\n')
                rfh2.write(line2_1+line2_2[F_trim:-1*B_trim]+'\n'+line2_3+line2_4[F_trim:-1*B_trim]+'\n')
if B_trim==0:
        if len(line1_2[F_trim:])>=50 and line2_2[F_trim:]>=50:
                rfh1.write(line1_1+line1_2[F_trim:]+'\n'+line1_3+line1_4[F_trim:]+'\n')
                rfh2.write(line2_1+line2_2[F_trim:]+'\n'+line2_3+line2_4[F_trim:]+'\n')
rfh1.close()
dfh1.close()
rfh2.close()
dfh2.close()
