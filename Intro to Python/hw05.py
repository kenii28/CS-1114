#!C:/python27/python.exe
'''
cs1114 

Submission: hw05

Programmer: Kenneth Huynh
Username: kh1983

Purpose of program, assumptions, constraints:

This module contains the function for hw05.
'''

def getCommonPositions(firstList, secondList):
    '''this function returns a list of two lists that gives the indicies of the
    common elemnts within the two lists passed in.'''
    commonPositions1 = []
    commonPositions2 = []
    for loopVar1 in range(len(firstList)):
        for loopVar2 in range(len(secondList)):
            if firstList[loopVar1] == secondList[loopVar2]:
                if loopVar1 not in commonPositions1:
                    commonPositions1.append(loopVar1)
                if loopVar2 not in commonPositions2:
                    commonPositions2.append(loopVar2)
    return [commonPositions1, commonPositions2]

