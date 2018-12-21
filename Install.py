print "----------------------------------------------------------------------------------------------------------------------------------------------------------"
print "TAURS-MH is dependent on Bismark, PICARD, python, bowtie, pysam,and samtools. Please make sure you have all of these on your system and provide path for installation."
print "You can always do this process again if you have typed wrong path or changed path of any program."
print "----------------------------------------------------------------------------------------------------------------------------------------------------------"
print "\n\n"
print "Please provide path to picard:"
picard=raw_input()
print "Please provide path to bismark:"
bismark=raw_input()
print "Please provide path to bowtie: "
bowtie=raw_input()
print "Please provide path to python: "
python=raw_input()

import os
TAURUS_loc=os.popen('pwd').read()

rfh=open("TAURUS-MH.py",'w')
dfh=open("template.py",'r')

count=0

for i in dfh:
	if count==6:
		rfh.write('picard="'+picard+'"\nbismark="'+bismark+'"\nbowtie="'+bowtie+'"\npython="'+python+'"\nTAURUS_loc="'+TAURUS_loc.rstrip()+'"\n')
	rfh.write(i)
	count+=1
