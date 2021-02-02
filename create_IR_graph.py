#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 José González ~ All rights reserved.
# Make IR graph run with ORCA

# jgonzalez76: Import librarys
import sys
import os
import matplotlib.pyplot as plt

# jgonzalez76: Change Font
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']

# jgonzalez76: Orca directory
orca_dir = "C:\\Orca\\orca.exe"

freq = []
value = []

if os.path.exists(orca_dir):
        # jgonzalez76: Make file graph
    os.system("orca_mapspc " + sys.argv[1] + " ir -x0400 -x14000 -n4000 -w10")
    dat = sys.argv[1] + ".ir.dat"

    # jgonzalez76: Extract information plot
    if os.path.exists(dat):
        with open(dat) as data:
            for line in data.readlines():
                x, y = line.split()
                freq.append(float(x))
                value.append(float(y))

        # jgonzalez76: plot IR spectrum
        plt.plot(freq, value, color="red")
        plt.title("IR spectrum")
        plt.xlim(4000, 400)
        plt.xlabel("Frequency")
        plt.ylabel("Transmittance (%)")
        plt.yticks([])
        plt.ylim(650, 1010)
        plt.show()
