import csv
import numpy as np

# this method is used so that the array representation of my csv file is not in scientific notation
np.set_printoptions(suppress=True)
# we are opening the csv file and reading it to extract the data
# we extracted the column that contains the sales value
file = 'Sales_01_20.csv'
data1 = np.loadtxt(file, delimiter=',', skiprows=1, usecols=1)


data2 = np.loadtxt(file, delimiter=',', skiprows=1)


# calculate Mean & Std of each year and print it
yearCount = 2001
meanArr = []
while(yearCount < 2021):
    for row in data2:
        if row[0] == yearCount:
            meanArr.append(row[1])
            continue
    mean = np.mean(meanArr)
    std = np.std(meanArr)
    strStd = ("%.3f" % std)
    strMean = ("%.3f" % mean)
    print('Mean for year: ' + str(yearCount) + ' = ' + strMean)
    print('Standard Dev for year: ' + str(yearCount) + ' = ' + strStd + '\n')
    meanArr.clear()
    yearCount += 1
    continue









# this project is the death of me



# now we extract all the data that exist within the csv file

