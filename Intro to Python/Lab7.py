#!C:/python27/python.exe
'''
Kenneth Huynh N18178828
This program is for rec07.
'''

from __future__ import print_function
import random

# PART ZERO
VALID1 = range(11)
VALID2 = ('#', '%', '@')


def getUserChar():
    '''this function returns a character inputted by the user'''
    userChar = raw_input('Enter the character: ')
    tooLong = len(userChar) != 1
    while userChar not in ('0','1','2','3','4','5','6','7','8','9', '#', '%', '@')  and tooLong:
        userChar = raw_input('Sorry, try again ')
    return userChar

def checkValidDigit():
    '''this function checks if the user's character is valid, which it is when
    it is within 2 of a passed in middle digit and prints it'''
    userChar = getUserChar()
    midDigit = random.randint(2,7)
    if userChar in ('0','1','2','3','4','5','6','7','8','9'):
        userChar = int(userChar)
        if (userChar in (midDigit - 2, midDigit - 1, midDigit, midDigit + 1, midDigit + 2)):
            print(userChar)
    elif userChar in ('#', '%', '@'):
        print(userChar)

def main():
    # PART ZERO MAIN
    '''while True:
       checkValidDigit()'''

    # PART ONE MAIN
    playKiosk()

    # PART TWO MAIN
    # printPsychedelic()
    

###########################################
    # PART ONE

def getNumTimesPlay():
    numTimes = raw_input('Enter the number of times to play: ')
    return int(numTimes)

def getName():
    name = raw_input('Enter your name: ')
    return name

def playGameNumTimes(numTimes, name):
        for game in range(numTimes):
            checkValidDigit()
            

def playKiosk():
    while True:
        numTimes = getNumTimesPlay()
        name = getName()
        if name in ('Joe', 'Sally', 'Bob'):
            exit()
            print('Please restart the machine after the maintenance is finished.')
        else: #isnt a manager
            playGameNumTimes(numTimes, name)
        print('Thanks,', name)





###########################################
    # PART TWO

def printPsychedelic():
    while True:
        print('>>>>><<<<<<<%%%%%&&&&&&&', end = '')

    



if __name__ == '__main__':
    main()

