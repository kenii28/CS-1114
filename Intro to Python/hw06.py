#!C:/python27/python.exe
'''
cs1114 

Submission: hw06

Programmer: Kenneth Huynh
Username: kh1983

Purpose of program, assumptions, constraints:

This program is for hw06.
'''

from __future__ import print_function


def getValidTrans():
    '''gets a valid positive number of at least one otherwise the user will be
    asked to enter another number'''
    numTrans = int(raw_input('How many transmissions to process? '))
    while numTrans < 1:
        numTrans = int(raw_input('Sorry must be 1 or more. Try again: '))
    return numTrans

def getData():
    '''gets the data the number of times past in. it also calculates the number
    of temperatures processed, percent rejected, average temp, max temp, min temp'''
    numTrans = getValidTrans()
    numDataSets = numTrans
    numAll = 0
    sumAll = 0
    allReject = 0
    MAXALL = -99999
    MINALL = 99999
    for data in range(numTrans):
        MAXDATA = -99999
        MINDATA = 99999
        STOP = 'STOP'
        numData = 0
        numReject = 0
        sumData = 0
        dataList = []
        numTrans = '1'
        setNum = data + 1
        print('Start entering data for set %i and indicate you are finished by typing STOP.' % (setNum))
        while numTrans != STOP:
            theData = raw_input()
            numTrans = theData
            if theData != STOP:
                theData = float(theData)
                if theData < -265.34205 or theData > -198.66205:
                    numReject += 1
                    print('[REJECTED: %f]' % (theData))
                else: #valid data entry
                    dataList.append(theData)
                    numData += 1
                    sumData += theData
                    if theData > MAXDATA:
                        MAXDATA = theData
                    if theData < MINDATA:
                        MINDATA = theData
        numAll += numData
        sumAll += sumData
        allReject += numReject
        if MAXDATA > MAXALL:
            MAXALL = MAXDATA
        if MINDATA < MINALL:
            MINALL = MINDATA
        print('\nData set %i' % (setNum))
        print('Stats:')
        if numData != 0:
            total = float(numReject + numData)
            percentReject = (float(numReject) / (total)) * 100
            averageTemp = float(sumData / numData)
            print('Number of temperatures processed: %i' % (numData))
            print('Percent rejected: %f' % (percentReject), end = '')
            print('%')
            print('Average temperature: %f' % (averageTemp))
            print('Maximum temperature: %f' % (MAXDATA))
            print('Minimum temperature: %f' % (MINDATA))
        else: #STOP without data
            print('''Number of temperatures processed: 0\n\
Percent rejected: 0%\n\
Average temperature: Not applicable\n\
Maximum temperature: Not applicable\n\
Minimum temperature: Not applicable''')
        print('\n')
    averageAll = sumAll / numAll
    rejectAll = (float(allReject) / float(allReject + numAll)) * 100
    print('End Processing\n')
    print('Number of data sets processed: %i' % (numDataSets))
    print('Average of all temperatures processed: %f' % (averageAll))
    print('Maximum Temperature: %f' % (MAXALL))
    print('Minimum Temperature: %f' % (MINALL))
    print('Percent rejected data: %f' % (rejectAll), end = '')
    print('%')
    
            
        
            


def main():
    getData()








if __name__ == '__main__':
    main()
