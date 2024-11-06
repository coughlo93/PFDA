# simple program to read a csv file as a dictionary
# Author : Owen Coughlan

import csv

DATADIR = "../lecture_1/"
FILENAME = "data.csv"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter="," , quoting=csv.QUOTE_ALL)
 
    total = 0
    for line in reader:
        print (line)