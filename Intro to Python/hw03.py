#!C:/python27/python.exe
'''
cs1114 

Submission: hw02

Programmer: Kenneth Huynh
Username: kh1983

Purpose of program, assumptions, constraints:

This program plays the hit and match game continuously until there is an error
or the user ends the program. This program assumes that user knows only to input
the integers between 0,9 inclusive.
'''
from __future__ import print_function
import random
import sys

def chooseHouseDigits():
    '''this function randomly generates three integers [0,9] for the house: left,
    middle, and right. then returns these three integers in that order'''
    leftDigit = random.randint(0,9)
    midDigit = random.randint(0,9)
    rightDigit = random.randint(0,9)
    return leftDigit, midDigit, rightDigit

def checkSameDigits(digitOne, digitTwo, digitThree):
    '''this function checks if any of the two given parameters are the same and returns
    True if there is a pair of the same number and False if there is not'''
    return ((digitOne == digitTwo) or (digitOne == digitThree) or (digitTwo == digitThree))
    
def askUserGuesses():
    '''this function asks the user for his or her left, mid, and right guesses
    for the randomly generated digits of the house'''
    leftGuess = int(raw_input('Enter digit for left position: '))
    midGuess = int(raw_input('Enter digit for middle position: '))
    rightGuess = int(raw_input('Enter digit for right position: '))
    return (leftGuess, midGuess, rightGuess)

def checkForHits(leftDigit, midDigit, rightDigit, leftGuess, midGuess, rightGuess):
    '''this function returns the number of hits'''
    hitCounter = 0
    if leftDigit == leftGuess :
        hitCounter += 1
    if midDigit == midGuess :
        hitCounter += 1
    if rightDigit == rightGuess :
        hitCounter += 1
    return hitCounter
    

def checkForMatches(leftDigit, midDigit, rightDigit, leftGuess, midGuess, rightGuess):
    '''this function returns the number of matches'''
    matchCounter = 0
    if (leftGuess == midDigit):
        matchCounter += 1
    if (leftGuess == rightDigit):
        matchCounter += 1
    if (midGuess == leftDigit):
        matchCounter += 1
    if (midGuess == rightDigit):
        matchCounter += 1    
    if (rightGuess == leftDigit):
        matchCounter += 1
    if (rightGuess == midDigit):
        matchCounter += 1
    return matchCounter

def displayHitsNMatch(hitCounter, matchCounter):
    '''this function displays the number of hits and matches'''
    if (hitCounter != 1):
        print (hitCounter, 'hits')
    else: #hitCounter == 1
        print ('1 hit')
    if (matchCounter != 1):
        print (matchCounter, 'matches')
    else: #matchcounter == 1
        print ('1 match')

def welcomeUser():
    '''this function welcomes the user to the game'''
    print('Welcome to the Hit && Match Game\nhit any key to start playing...')
    raw_input('')
    
def sayByeToUser():
    '''this function says come back and play sometime to the user'''
    print('Come back and play again sometime\n')

def playOneHitAndMatchGame():
    welcomeUser()
    leftDigit, midDigit, rightDigit = chooseHouseDigits()
    areThereSame1 = checkSameDigits(leftDigit, midDigit, rightDigit)
    if areThereSame1:
        print('We are sorry but the game has malfunctioned.\nEnding...')
        sys.exit(17)
    leftGuess, midGuess, rightGuess = askUserGuesses()
    areThereSame2 = checkSameDigits(leftGuess, midGuess, rightGuess)
    if areThereSame2:
        print('Sorry, that is an invalid try.')
        sayByeToUser()
        pass
    else: #notSame
        numHits = checkForHits(leftDigit, midDigit, rightDigit, leftGuess, midGuess, rightGuess)
        numMatches = checkForMatches(leftDigit, midDigit, rightDigit, leftGuess, midGuess, rightGuess)
        displayHitsNMatch(numHits, numMatches)
        sayByeToUser()

def main():
    while True:
        playOneHitAndMatchGame()


if __name__ == '__main__':
    main()
