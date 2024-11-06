import csv
import os

DATADIR = "C:/Users/owenc/Desktop/PFDA/my-work/lecture_1/lab_1/"
FILENAME = "data.csv"

# Check if the file exists before opening
print("File exists:", os.path.exists(DATADIR + FILENAME))

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    for line in reader:
        print(line)