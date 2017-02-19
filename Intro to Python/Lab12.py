#!C:/python27/python.exe
'''
Kenneth Huynh N18178828
This program is for rec12.
'''
from __future__ import print_function
import os

#PART ONE
def getInputFile():
    '''asks the user to pick an input file name'''
    inputFile = raw_input('Enter the input file name: ') + '.txt'
    while not os.path.exists(inputFile):
        inputFile = raw_input('Not valid file, try again: ')
    fh = open(inputFile, 'r')
    return fh
def getOutputFile():
    '''asks the user to pick an output file name'''
    handleChoice = 'N'
    while handleChoice.lower() == 'n':
        outputFile = raw_input('what would you like the output file to be?') + '.txt'
        if os.path.exists(outputFile):
            handleChoice = raw_input('A file with this name already exists. want to overwrite?')
        else:
            handleChoice = 'Y'
    outFile = open(outputFile, 'w')
    return outFile
    
def getBetweenString():
    '''asks the user to pick a between string'''
    btwnString = raw_input('Enter a between string: ')
    return btwnString

def processInputFile(inputFile, outputFile, betweenString):
    '''gets the contents of the inputFile and replaces all spaces with the
    between string and then writes it to the outputFile.'''
    for line in inputFile:
        lineList = line.split()
        outputLine = betweenString.join(lineList)
        outputFile.write(outputLine + '\n')
    inputFile.close()
    outputFile.close()

def pauseFunction():
    '''this function pauses the screen for the user.'''
    raw_input()

##def main():
##    inputFile = getInputFile()
##    outputFile = getOutputFile()
##    betweenString = getBetweenString()
##    processInputFile(inputFile, outputFile, betweenString)
##    pauseFunction()



#PART TWO
def undoProcessInput(betweenString):
    '''undoes what processInputFile did'''
    inputFile = getInputFile()
    outputFile = getOutputFile()
    inputString = inputFile.readlines()
    for line in inputString:
        lineList = line.split(betweenString)
        outputString = ' '.join(lineList)
        outputFile.write(outputString)
    inputFile.close()
    outputFile.close()

##def main():
##    betweenString = getBetweenString()
##    undoProcessInput(betweenString)
##    pauseFunction()

#PART THREE
def processRecord(inputFile, outputFile):
    '''processes a record in the format of
    project number (an int)
    data item (a float) 
    data item (a float) 
    data item (a float) 
    data item (a float) 
    *****
    then writes to the outputFile the project number followed by the average
    of the data items.
    '''
    projectNumber = inputFile.readline().strip()
    
    while projectNumber != '':
        while inputFile.readline().strip() != '*****':
            totalData = 0
            numData = 0
            dataItem = float(inputFile.readline().strip())
            totalData += dataItem
            numData += 1
            averageData = totalData / float(numData)
            outputLine = projectNumber + ': ' + str(averageData)
        outputFile.write(outputLine)
        projectNumber = inputFile.readline().strip()

def main():
    inputFile = getInputFile()
    outputFile = getOutputFile()
    processRecord(inputFile, outputFile)

#PART FOUR
def processRecordAndReject(inputFile, outputFile):
    '''processes a record in the format of
    project number (an int)
    data item (a float) 
    data item (a float) 
    data item (a float) 
    data item (a float) 
    *****
    then writes to the outputFile the project number followed by the average
    of the data items.
    invalid records will be added to a file called reject.txt
    '''
    projectNumber = inputFile.readline().strip()
    if '7' not in projectNumber:
        rejectfh = open('reject.txt', 'w')
        totalData = 0
        numData = 0
        dataItem = float(inputFile.readline().strip())
        totalData += dataItem
        numData += 1
        averageData = totalData / float(numData)
        outputLine = projectNumber + ': ' + str(averageData)
        rejectfh.write(outputLine)
    else: #valid projectNumber
        while projectNumber != '':
            while projectNumber != '*****':
                totalData = 0
                numData = 0
                dataItem = float(inputFile.readline().strip())
                totalData += dataItem
                numData += 1
                averageData = totalData / float(numData)
                outputLine = projectNumber + ': ' + str(averageData)
            outputFile.write(outputLine)
            projectNumber = inputFile.readline().strip()    

##def main():
##    inputFile = getInputFile()
##    outputFile = getOutputFile()
##    processRecordAndReject(inputFile, outputFile)


if __name__ == '__main__':
    main()

        
    
        
    
