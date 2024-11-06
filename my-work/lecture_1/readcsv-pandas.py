# reading in CSV as a pandas table
# Author : Owen Coughlan



DATADIR = "../lecture_1/"
FILENAME = "data.csv"

import pandas
df = pandas.read_csv(DATADIR + FILENAME)
print (df)
