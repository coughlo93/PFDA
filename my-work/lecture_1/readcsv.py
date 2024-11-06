# simple program to read a csv file
# Author : Owen Coughlan

import csv

DATADIR = "../lecture_1/"
FILENAME = "data.csv"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter="," , quoting=csv.QUOTE_ALL)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: # first row ie header rown
            print(f"{line}\n------------")
    else: # all subsequent rows
        total += int(line[0])
        print (line)
        linecount += 1