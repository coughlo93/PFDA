# read in a simple file
# Author: Owen Coughlan

FILENAME = "data.txt"
DATADIR = "../lecture_1/"

print (DATADIR + FILENAME)
with open(DATADIR + FILENAME, "rt") as fp:
    total = 0
    for line in fp:
        total +- int(line)
        print (line, end="")
    print (f"total is {total}")