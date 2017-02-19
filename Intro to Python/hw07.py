#!C:/python27/python.exe
'''
cs1114 

Submission: hw07

Programmer: Kenneth Huynh
Username: kh1983

Purpose of program, assumptions, constraints:

This program is for hw07.
'''

from __future__ import print_function

SENT_LIST = ['Botty', 'Roboat', 'Borot']

def updateValueAtKey( dicty, keyVal, floatToAdd ):
    ''' Takes a dictionary of str -> float key/value pairs.
        Assume that this kind of dictionary will be passed in.
        Adds the floatToAdd value to the float value in the
        dictionary at keyVal.
        E.g.: if dicty['john'] is  12.22 and the call:
        updateValueAtKey( dicty, 'john', 100 ) is made, 
        then, after the call, dicty['john'] is 112.22
        If the key is not in the dictionary, inserts the
        the key/value pair: keyVal -> floatToAdd
        into the dictionary. '''
    if keyVal in dicty:
        dicty[keyVal] += floatToAdd
    else: #keyVal not in dicty
        dicty[keyVal] = floatToAdd

def welcomeMessage():
    '''a welcoming message for the snakenicker'''
    print('Welcome Snakenicker')

def askAndGetName():
    '''asks the user for their name and returns their name'''
    userName = raw_input('What is your name?\n')
    return userName

def askNumDonation():
    '''asks the user for the number of donations they would like to enter
    and returns that number'''
    numDonation = int(raw_input('How many donations? '))
    return numDonation

def getDonAmtFromStd(userName, numDonation, dicty):
    '''gets all the donation amounts from the students and updates the
    amount corresponding to their name in the dictionary'''
    sumDonation = 0
    for donateTimes in range(numDonation):
        donationAmount = float(raw_input())
        sumDonation += donationAmount
    updateValueAtKey(dicty, userName, sumDonation)

def printStudentDonationData(dicty):
    '''prints everyone's donation. first their name followed by the total amount
    in alphabetical order'''
    print('''Everyone's donations:\n''')
    sortedKeys = dicty.keys()
    sortedKeys.sort()
    for name in sortedKeys:
        print(name, '$', dicty[name])
    
def pauseScreen():
    '''pauses the screen for user to see the results'''
    raw_input()

    
def main():
    donationDict = {}
    welcomeMessage()
    userName = raw_input('What is your name?\n')
    while userName not in SENT_LIST:
              numDonation = askNumDonation()
              getDonAmtFromStd(userName, numDonation, donationDict)
              welcomeMessage()
              userName = askAndGetName()
    printStudentDonationData(donationDict)
    pauseScreen()




if __name__ == '__main__':
    main()
