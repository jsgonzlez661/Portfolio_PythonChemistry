#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 José González ~ All rights reserved.
# Extract chemical shielding run with ORCA

# jgonzalez76: Import librarys
import sys
import os

# jgonzalez76: Definition of the variables
nmr_c13 = []
nmr_h1 = []
select_vibration = []

# jgonzalez76: Definition of the constants
b3lyp_c13 = [190.12, 192.03, 190.27, 182.99]
b3lyp_h1 = [32.17, 31.73, 31.57, 32.04]

pbe0_c13 = [195.04, 196.77, 194.49, 188.09]
pbe0_h1 = [32.12, 31.66, 31.48, 31.87]

m062x_c13 = [187.97, 188.79, 187.47, 180.17]
m062x_h1 = [32.22, 31.67, 31.49, 31.87]

print('\nB3LYP')
print(b3lyp_c13)
print(b3lyp_h1)
print('\nPBE0')
print(pbe0_c13)
print(pbe0_h1)
print('\nM06-2X')
print(m062x_c13)
print(m062x_h1)

select_func = int(input("\nSelect functional for ajustement\n1. B3-LYP\n2. PBE0\n3. M06-2X\n"))
tms_value = int(input("Select TMS value -> 0,1,2,3\n"))
    
# jgonzalez76: Data extraction 
with open(sys.argv[1], 'r') as file:
    for line in reversed(file.readlines()):
        try:    
            if(line.split()[1]=='H'):
                nmr_h1.append(line.split()[0:3])
            elif(line.split()[1]=='C'):
                nmr_c13.append(line.split()[0:3])
            elif('  -------  -------  ------------   ------------' in line):
                break
        except IndexError:
            pass

# jgonzalez76: Inversed lists 
nmr_h1 = nmr_h1[::-1]       
nmr_c13 = nmr_c13[::-1] 
            
with open(sys.argv[1]+'_NMR.txt', 'w') as file:
    file.write("Script Create for Jose Gonzalez\n")
    file.write("Contact jgonzalez76@uc.edu.ve\n")
    file.write("--------------------------------\n")
    file.write("CHEMICAL SHIELDING SUMMARY (ppm)\n")
    file.write("--------------------------------\n")
    if(select_func == 1):
        h_value = b3lyp_h1[tms_value]
        c_value = b3lyp_c13[tms_value]
    if(select_func == 2):
        h_value = pbe0_h1[tms_value]
        c_value = pbe0_c13[tms_value]
    if(select_func == 3):
        h_value = m062x_h1[tms_value]
        c_value = m062x_c13[tms_value]
        
    for line in nmr_c13:
        c13_correct = round(c_value - float(line[2]), 2)
        file.write(line[1] + str((int(line[0])+1)) +'\t\t'+ line[2]+'\t\t'+ str(c13_correct)+'\n')
    for line in nmr_h1:
        h1_correct = round(h_value - float(line[2]), 2)
        file.write(line[1] + str((int(line[0])+1)) +'\t\t'+ line[2]+'\t\t'+ str(h1_correct)+'\n')

