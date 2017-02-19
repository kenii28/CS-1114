#!C:/python27/python.exe
'''
cs1114 

Submission: hw04

Programmer: Kenneth Huynh
Username: kh1983

Purpose of program, assumptions, constraints:

This module contains the function for hw04.
'''


def getCommonElements(firstList, secondList):
    '''this function returns a list of all the same elements within the lists
    passed into the function'''
    commonElements = []
    for loopVar in firstList:
        if loopVar in secondList:
            if loopVar not in commonElements:
                commonElements.append(loopVar)
    return commonElements

