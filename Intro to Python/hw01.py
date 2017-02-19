'''
Kenneth Huynh (N18178828)
This module contains functions to create flags.
'''

from __future__ import print_function

thePole = '|'

def printTopOfPole():
    '''prints the top of the pole of the flag'''
    print('^')

def printPoleBottom():
    '''prints the 2 pieces of the pole for the bottom'''
    print('\n|\n|')

def printFifteenWithPole(theChar):
    '''prints 15 of the character with pole and with new line'''
    print(thePole, theChar * 15, sep = '')
    
def printFive(theChar):
    '''prints 5 of the character given without going to the next line'''
    print(theChar * 5, end = '')

def printFiveWithNewLine(theChar):
    '''prints 5 of the character given with next line'''
    print(theChar * 5)
    
def printFiveWithPole(theChar):
    '''prints the pole first then 5 of the given character without going to the next time'''
    print(thePole, end = '')
    printFive(theChar)
    
def printAlternating(firstChar, secondChar):
    '''prints the first character then the second then the first then the second then the first'''
    print(firstChar, secondChar, firstChar, secondChar, firstChar, sep = '', end = '')

def printAlternatingWithNewLine(firstChar, secondChar):
    '''prints the first character then the second then the first then the second then the first with a new line'''
    print(firstChar, secondChar, firstChar, secondChar, firstChar, sep = '')

def printAlternatingWithPole(firstChar, secondChar):
    '''prints the first character then the second then the first then the second then the first'''
    print(thePole, firstChar, secondChar, firstChar, secondChar, firstChar, sep = '', end = '')

def printFiveThenTenWithPole(firstChar, secondChar):
    '''prints 5 of the first character then 10 of the second character without a space'''
    print(thePole, end = '')
    printFive(firstChar)
    printFive(secondChar)
    printFiveWithNewLine(secondChar)
    
