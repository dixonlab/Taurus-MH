import sys
import gzip
chro_order=[]
for i in range(1,24):
        chro_order.append('chr'+str(i))
chro_order.append('chrX')
chro_order.append('chrY')
chro_order.append('chrM')

chro_order='1 2 3 4 5 6 7 X 8 9 10 11 12 13 14 15 16 17 18 20 Y 19 22 21'.split()
fn1=sys.argv[1]
fn2=sys.argv[2]
sample_name1=fn1.split('_')[4]+'_'+'_'.join(fn1.split('_')[9:12])
sample_name2=fn2.split('_')[4]+'_'+'_'.join(fn2.split('_')[9:12])
dfh1=gzip.open(fn1,'r')                                                                                          
dfh2=gzip.open(fn2,'r')
rfh=open(sys.argv[3],'w')
rfh.write('index\t'+sample_name1+'\t'+sample_name2+'\n')
index1=0
index2=0
for i in dfh1:
        line=i.split()
        chro=line[0]
        pos=line[1]
        if chro in chro_order:
                index1=chro_order.index(chro)*10000000000+int(pos)
                ID1='chr'+line[0]+':'+line[1]+'_'+line[2]+'_'+line[3]
                data1=str(round(100*float(line[4])/float(line[5]),2))+'('+line[4]+','+line[5]+')'
        if chro not in chro_order:
                index1=100000000000
        if index1>index2:
                for a in dfh2:
                        line2=a.split()
                        chro=line2[0]
                        pos=line2[1]
                        if chro in chro_order:
                                index2=chro_order.index(chro)*1000000000+int(pos)
                                ID2='chr'+line[0]+':'+line[1]+'_'+line[2]+'_'+line[3]
                                data2=str(round(100*float(line[4])/float(line[5]),2))+'('+line[4]+','+line[5]+')'
                                if index2<index1:
                                        if ID2.split('_')[-1][:2]=='CG':
                                                rfh.write(ID2+'\tNA\t'+data2+'\n')
                                if index2>=index1:
                                        break
                        if chro not in chro_order:
                                index2=100000000000
        if index1==index2:
                if ID1.split('_')[-1][:2]=='CG':
                        rfh.write(ID2+'\t'+data1+'\t'+data2+'\n')
        if index1<index2:
                if ID1.split('_')[-1][:2]=='CG':
                        rfh.write(ID2+'\t'+data1+'\tNA\n')
        if index1==100000000000 and index2==100000000000:
                break
for i in dfh2:
        line=i.split()
        chro=line[0]
        pos=line[1]
        if chro in chro_order:
                index2=chro_order.index(chro)*10000000000+int(pos)
                ID2='chr'+line[0]+':'+line[1]+'_'+line[2]+'_'+line[3]
                data2=str(round(100*float(line[4])/float(line[5]),2))+'('+line[4]+','+line[5]+')'
        if chro not in chro_order:
                index2=100000000000
        if index1==index2:
                if ID1.split('_')[-1][:2]=='CG':
                        rfh.write(ID2+'\t'+data1+'\t'+data2+'\n')
        if index1<index2:
                if ID1.split('_')[-1][:2]=='CG':
                        rfh.write(ID2+'\t'+data1+'\tNA\n')
        if index2<index1:
                if ID2.spit('_')[-1][:2]=='CG':
                        rfh.write(ID2+'\tNA\t'+data2+'\n')
        if index2==100000000000:
                break          
