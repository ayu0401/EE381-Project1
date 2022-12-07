import csv
import numpy as np

# we are opening the csv file and reading it to extract the data
file = 'Sales_01_20.csv'
data = np.loadtxt(file, delimiter=',', skiprows=1, dtype=int, usecols=1)
print(data)





# now we extract all the data that exist within the csv file

