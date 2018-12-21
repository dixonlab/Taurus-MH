# Taurus-MH

Introduction

TAURUS-MH (Two-step Alignment with Unmapped Reads Using read Splitting for Methyl-HiC) is a mapping pipeline for methyl-3C/methyl-HiC data using a hybrid of ungapped and manual read splitting alignments with Bismark and Bowtie1.

TAURUS-MH is dependent on Bismark, Bowtie1, PICARD, python, and pysam (a python module).

To install TAURUS-MH, Simply download all the python codes and run:
python Install.py

The Install program will ask you path to picard, bismark, bowtie, and python. Please provide correct path to these.
After the installation, TAURUS-MH.py will be generated.

You can run TAURUS-MH with cmd:
python TAURUS-MH.py <genome_folder> <G to A converted mate> <C to T converted mate>  
