#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 José González ~ All rights reserved.
# Extract bond lengths and angles from a geometric optimization run with ORCA

# jgonzalez76: Import librarys
import os
import sys

# jgonzalez76: Definition of the variables
valores_enlaces = []
num_enlace = []
valores_angulos = []
num_angulo = []

try:
    # jgonzalez76: Data extraction 
    file_name = sys.argv[1]
    with open(file_name, 'r') as out:
        j = 0
        for line in out:
            if("HURRAY" in line):
                for i in range(0, 12):
                    out.readline()
                while(1):
                    l = out.readline()
                    if(l.split()[1].split()[0][0] == "D"):
                        break
                    if(l.split()[1].split()[0][0] == "B"):
                        num_enlace.append(l.split()[0:4])
                        valores_enlaces.append(l.split()[7])
                    if(l.split()[1].split()[0][0] == "A"):
                        num_angulo.append(l.split()[0:5])
                        valores_angulos.append(l.split()[8])

    with open('listBAatom_' + file_name.split('.')[0] + '.txt', 'w') as listDistance:
        with open('listBAatom_' + file_name.split('.')[0] + '.csv', 'w') as listDistance2:

            listDistance.write("Script Create for Jose Gonzalez\n")
            listDistance.write("Contact jgonzalez76@uc.edu.ve\n")
            listDistance.write("\nLengths and angles of bonds for " + file_name + '\n')
            
            # jgonzalez76: Generates .csv and .txt files 
            
            j = 0
            for i in num_enlace:
                BondAT_1 = i[2].split(',')[1] + str(int(i[3].split(')')[0]) + 1)
                BondAT_2 = i[1].split('(')[1] + str(int(i[2].split(',')[0]) + 1)
                escribir = BondAT_1 + '-' + BondAT_2 + '\t\t' + valores_enlaces[j]
                listDistance.write(escribir + '\n')
                listDistance2.write(escribir.replace('\t\t', ';') + '\n')
                j += 1

            z = 0
            for w in num_angulo:
                AngleAT_1 = w[1].split(
                    '(')[1] + str(int(w[2].split(',')[0]) + 1)   # primer atomo
                AngleAT_2 = w[2].split(',')[1] + \
                    str(int(w[3].split(',')[0]) + 1)
                AngleAT_3 = w[3].split(
                    ',')[1] + str(int(w[4].split(')')[0]) + 1)   # tercer atomo
                escribir2 = AngleAT_1 + '-' + AngleAT_2 + '-' + \
                    AngleAT_3 + '\t\t' + valores_angulos[z]
                listDistance.write(escribir2 + ' \n')
                listDistance2.write(escribir2.replace('\t\t', ';') + '\n')
                z += 1

    print("\nMAKE FILE CREATE SUCESSFULLY\n")
    
except IndexError:
    print("\nINVALID FILE\n")
    sys.exit(0)
