import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

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
finalStd = []
finalMean = []
finalPrc = []
years = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,
         2015, 2016, 2017, 2018, 2019, 2020]

while (yearCount < 2021):
    houseSold = 0
    for row in data2:
        if row[0] == yearCount:
            if 200000 <= row[1] <= 300000:
                houseSold += 1
            meanArr.append(row[1])
            continue
    mean = np.mean(meanArr)
    finalMean.append(mean)
    std = np.std(meanArr)
    finalStd.append(std)
    strStd = ("%.3f" % std)
    strMean = ("%.3f" % mean)
    print('Mean for year: ' + str(yearCount) + ' = ' + strMean)
    print('Standard Dev for year: ' + str(yearCount) + ' = ' + strStd)

    # probability calculated here
    prob = houseSold / len(meanArr)
    prob = prob * 100
    finalPrc.append(prob)
    strProb = ("%.3f" % prob)
    print('Probability of Houses Sold from $200,000 - $300,000 from year: ' + str(yearCount)
          + ' = ' + strProb + '%' + '\n')
    meanArr.clear()
    yearCount += 1
    continue

# this project is the death of me
# MEAN BAR GRAPH
fig, ax = plt.subplots()
ax.set_title('Mean of Every Year')
ax.set_xlabel('Year')
ax.set_ylabel('Mean Price for Houses $$$', labelpad=-1)
ax.set_yticks(np.arange(0, 800000, 50000))
ax.set_xticks(years, rotation=90)
ax.tick_params(axis='x', which='major', labelsize=5.4)
ax.bar(years, finalMean, color='r', width=0.5)

# STD BAR GRAPH
fig2, ax2 = plt.subplots()
ax2.set_title('Standard Dev of Every Year')
ax2.set_xlabel('Year')
ax2.set_ylabel('Standard Deviation')
ax2.set_xticks(years, rotation=90)
ax2.set_yticks(np.arange(0, 6000000, 1000000))
ax2.ticklabel_format(style='plain')
ax2.tick_params(axis='x', which='major', labelsize=5.4)
ax2.bar(years, finalStd, color='b', width=0.5)

# PROBABILITY BAR GRAPH
fig3, ax3 = plt.subplots()
ax3.set_title('Probability of House Cost Between $200,000 and $300,000')
ax3.set_xlabel('Year')
ax3.set_ylabel('Probability in Percentage')
ax3.set_xticks(years, rotation=90)
ax3.set_yticks(np.arange(10, 50, 10))
ax3.yaxis.set_major_formatter(ticker.PercentFormatter())
ax3.tick_params(axis='x', which='major', labelsize=5.4)
ax3.bar(years, finalPrc, color='g', width=0.5)
plt.show()
# calculate the yearly probabilities of sales prices ranging from $200,000 - $300,000 inclusive
