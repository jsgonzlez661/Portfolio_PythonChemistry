#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 José González ~ All rights reserved.
# Extract the vibrational frequencies run with ORCA

# jgonzalez76: Import librarys
import sys

# jgonzalez76: Definition of the scale factors
b3lyp = [0.9632, 0.9607, 0.9640, 0.9665]
pbe0 = [0.9502, 0.9488, 0.9530, 0.9564]
m062x = [0.9464, 0.9445, 0.9484, 0.9505]

try:
    file = sys.argv[1]
    select_vibration = []
    print("List of Scale Factor")
    print("B3-LYP:")
    print(b3lyp)
    print("\nPBE0:")
    print(pbe0)
    print("\nM062X:")
    print(m062x)
    select_func = int(
        input("\nSelect functional for Scale Factor\n1. B3-LYP\n2. PBE0\n3. M06-2X\n"))
        
    with open(file, 'r') as data:
        i = 0
        list_vibration = []
        j = 1
        for line in reversed(data.readlines()):
            i += 1
            if("freq." in line):
                list_vibration.append(float(line.split()[1]))
                j += 1
    scale_f = int(input("Select Scale Factor position -> 0,1,2,3\n"))
    
    with open('frecuencies.txt', 'w') as file_freq:    
        list_freq = list_vibration[::-1]
        file_freq.write("Script Create for Jose Gonzalez\n")
        file_freq.write("Contact jgonzalez76@uc.edu.ve\n")
        file_freq.write("\n-----------------------\nVIBRATIONAL FREQUENCIES\n-----------------------\n")
        file_freq.write("Total Frecuencies: " + str(len(list_freq)))
        file_freq.write("\n\nNo scaling\t Scaling\n")
        
        for freq in list_freq:
            if(select_func == 1):
                file_freq.write(str(round(freq, 2)) + "\t\t" +
                      str(round(freq * b3lyp[scale_f], 2))+'\n')
            if(select_func == 2):
                file_freq.write(str(round(freq, 2)) + "\t\t" +
                      str(round(freq * pbe0[scale_f], 2))+'\n')
            if(select_func == 3):
                file_freq.write(str(round(freq, 2)) + "\t\t" +
                      str(round(freq * m062x[scale_f], 2))+'\n')
                      
    print("\nMAKE FILE CREATE SUCESSFULLY\n")

except IndexError:
    print("Invalidate input file")

except FileNotFoundError:
    print("No such file or directory")

except KeyError:
    print("Vibration invalidate")
