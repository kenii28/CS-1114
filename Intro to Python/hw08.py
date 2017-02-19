#!C:/python27/python.exe
'''
cs1114 

Submission: hw08

Programmer: Kenneth Huynh
Username: kh1983

Purpose of program, assumptions, constraints:

This program is for hw08.
Works only with single word named countries.
Could not figure out how to ignore the spaces between countries like Antigua and Barbuda.

'''
import copy


def makePopulationSummary():
    '''reads a file of the population change of countries and writes to a file
    the summary of the data in the file.'''
    firstPeriod = []
    secondPeriod = []
    fhData = open('hw08data.txt', 'r')
    fh1990 = open('1970_1990_summary.txt', 'w')
    fh2007 = open('1990_2007_summary.txt', 'w')
    firstLine = fhData.readline()
    for line in fhData:
        split = line.strip().split()
        noComma = split[0].strip(',')
        percent = float(split[2].strip('%'))
        percentCountry = [percent, noComma]
        if split[1] == '1970-1990':
            firstPeriod.append(percentCountry)
        else: #1990-2007
            secondPeriod.append(percentCountry)
    firstSum = 0
    numFirst = 0
    secondSum = 0
    numSecond = 0
    for item in firstPeriod:
        firstSum += item[0]
        numFirst += 1
    for item in secondPeriod:
        secondSum += item[0]
        numSecond += 1
    firstAverage = firstSum / float(numFirst)
    secondAverage = secondSum / float(numSecond)
    firstCopy = copy.deepcopy(firstPeriod)
    secondCopy = copy.deepcopy(secondPeriod)
    for item in firstCopy:
        abs(item[0])
    for item in secondCopy:
        abs(item[0])
    firstCopy.sort()
    secondCopy.sort()
    firstSmallLarge = [firstCopy[0], firstCopy[1], firstCopy[2], firstCopy[-1], firstCopy[-2], firstCopy[-3]]
    secondSmallLarge = [secondCopy[0], secondCopy[1], secondCopy[2], secondCopy[-1], secondCopy[-2], secondCopy[-3]]
    withNegativeList1 = []
    withNegativeList2 = []
    for item in firstSmallLarge:
        idx = firstPeriod.index(item)
        withNegativeList1.append(firstPeriod[idx])
    for item in secondSmallLarge:
        idx = secondPeriod.index(item)
        withNegativeList2.append(secondPeriod[idx])
    fh1990.write('1970-1990 Summary Report\n\nAverage percent change over all: ')
    fh1990.write(firstAverage, '%\n\nThe three countries or regions with the largest change:\n')
    fh1990.write(withNegativeList1[-1][1], '(', withNegativeList1[-1][0], '%), ', withNegativeList1[-2][1], '(', withNegativeList1[-2][0], '%), ', withNegativeList1[-3][1], '(', withNegativeList1[-3][0], '%)\n')
    fh1990.write('The three countries or regions with the smallest change:\n')
    fh1990.write(withNegativeList1[-4][1], '(', withNegativeList1[-4][0], '%), ', withNegativeList1[-5][1], '(', withNegativeList1[-5][0], '%), ', withNegativeList1[-6][1], '(', withNegativeList1[-6][0], '%)\n')

    fh2007.write('1990-2007 Summary Report\n\nAverage percent change over all: ')
    fh2007.write(secondAverage, '%\n\nThe three countries or regions with the largest change:\n')
    fh2007.write(withNegativeList2[-1][1], '(', withNegativeList2[-1][0], '%), ', withNegativeList2[-2][1], '(', withNegativeList2[-2][0], '%), ', withNegativeList2[-3][1], '(', withNegativeList2[-3][0], '%)\n')
    fh2007.write('The three countries or regions with the smallest change:\n')
    fh2007.write(withNegativeList2[-4][1], '(', withNegativeList2[-4][0], '%), ', withNegativeList2[-5][1], '(', withNegativeList2[-5][0], '%), ', withNegativeList2[-6][1], '(', withNegativeList2[-6][0], '%)\n')

    fh1990.close()
    fh2007.close()
    fhData.close()
    
def main():
    makePopulationSummary()

if __name__ == '__main__':
    main()

        
    
        
