#!C:/python27/python.exe
'''
Kenneth Huynh N18178828
This program dispenses stamps and returns the change in coins. There is also a prize
the user can win after using the machine.
'''

from __future__ import print_function
import Lab4
import random
import Lab3

SEVENTYFOUR_STAMP = 0.74
THIRTYTWO_STAMP = 0.32
SIX_STAMP = 0.06

def printDashLine():
    '''prints - 44 times with a space in the beginning and end'''
    print(' ', '-' * 44, ' ', sep = '')

def printWelcomeStampLine():
    '''prints Welcome to the snakeStamp Machine! in the center of spaces and |'''
    print('|     Welcome to the snakeStamp Machine!     |')

def printDispenseOnlyLine():
    '''prints the we dispense only line'''
    print('| We dispense only 74, 32 and 6 cent stamps. |')

def printOnlyCoinsChangeLine():
    '''print the we only give coins in change line'''
    print('| We give only coins in change - (no bills). |')
    
def printStampHeading():
    printDashLine()
    printWelcomeStampLine()
    printDispenseOnlyLine()
    printOnlyCoinsChangeLine()
    printDashLine()
    print('\n')
    
def askFirstName():
    '''asks the user for their first name'''
    firstName = raw_input('What is your first name? ')
    return firstName

def askLastName():
    '''asks the user for their last name'''
    lastName = raw_input('What is your last name? ')
    print('\n')
    return lastName

def askNum74Stamps():
    '''asks the user for the number of 74 cent stamps they want'''
    num74Stamps = int(raw_input('How many 74 cent stamps would you like? '))
    return num74Stamps
    
def askNum32Stamps():
    '''asks the user for the number of 32 cent stamps they want'''
    num32Stamps = int(raw_input('How many 32 cent stamps would you like? '))
    return num32Stamps

def askNum6Stamps():
    '''asks the user for the number of 6 cent stamps they want'''
    num6Stamps = int(raw_input('How many 6 cent stamps would you like? '))
    print('\n')
    return num6Stamps

def printsPriceOfStamps(num74Stamps, num32Stamps, num6Stamps):
    '''prints the total price of stamps after calculating number of stamps and the total price'''
    numOfStamps = num74Stamps + num32Stamps + num6Stamps
    cost74Stamps = float(num74Stamps) * SEVENTYFOUR_STAMP
    cost32Stamps = float(num32Stamps) * THIRTYTWO_STAMP
    cost6Stamps = float(num6Stamps) * SIX_STAMP
    totalPrice = cost74Stamps + cost32Stamps + cost6Stamps
    print('The price of your %i stamps is $%.2f' % (numOfStamps, totalPrice))
    print('\n')
    return totalPrice

def askHowManyDollars():
    '''asks the user how many dollars will they be giving us'''
    numDollarsGiven = raw_input('How many dollars will you be giving us? ')
    print('\n')
    return numDollarsGiven

def printAMomentLine():
    '''prints the Thank you. Just a moment please line'''
    print('Thank you. Just a moment please...')
    print('\n')

def printThanksNameLine(firstName,lastName):
    '''prints the Thanks Name, your change is line'''
    print('Thanks %s %s, your change is:' % (firstName, lastName))

def printDashEqualLine():
    '''prints 3 - then 39 = then 3 -'''
    print('-' * 3, '=' * 39, '-' * 3, sep = '')

def printThankUseLine():
    '''print thank you for using our stamp machine line'''
    print('-' * 3, 'Thank you for using our stamp machine', '-' * 3)

def printThankYouEnding():
    '''prints the thank you at the end before the prize'''
    printDashEqualLine()
    printThankUseLine()
    printDashEqualLine()
    print('\n')

def printCongratsLine(firstName):
    '''prints the congrats line'''
    print('CONGRATULATIONS ', firstName, '!', sep = '')
    print('\n')

def printChosenLine():
    '''Tells the use that they have been chosen to evaluate the machine'''
    print('You have been chosen to help us evaluate our machine.')
    print('\n')

def askForRating():
    '''asks the user for their rating of the machine'''
    theRating = raw_input('''For helping you will have a chance to win a prize.\nPlease rate our machine by entering a number between 1 and 10,\nwith 10 being really great and 1 being horrible: ''')
    return theRating

def printThankYouLine():
    '''prints thank you line'''
    print('Thank you for using our stamp machine.')

def checkWhichPrize(theRating, totalPrice):
    '''checks which prize the user wins'''
    randomNumber = random.randint(1,1000)
    if randomNumber == theRating: #grand prize
        print('You won $50!!!')
    elif theRating in (2, 4, 7) or  (17.25 <= totalPrice <= 58.42): #first prize
        print('You won $2.33!!!')
    elif totalPrice > 1.37: #second prize
        print('You won 37 cents!!!')
    else: #consolation
        print('You won 3 cents!!!')

def printsRandomBanner():
    '''this function prints the random banner'''
    randChar = chr(random.randint(97,122))
    randNumLineSeg = random.randint(4,5)
    randNumChar = random.randint(4,6)
    Lab3.drawSlashBackSlashLine()
    print(randChar * randNumChar)
    Lab3.drawBackSlashSlashLine()
    
    



def main():
    #randombanner
    printStampHeading()
    firstName = askFirstName()
    lastName = askLastName()
    num74Stamps = askNum74Stamps()
    num32Stamps = askNum32Stamps()
    num6Stamps = askNum6Stamps()
    totalPrice = printsPriceOfStamps(num74Stamps, num32Stamps, num6Stamps)
    numDollars = askHowManyDollars()
    printAMomentLine()
    printThanksNameLine(firstName, lastName)
    Lab4.printAsCoins(totalPrice)
    print('\n')
    printThankYouEnding()
    printCongratsLine(firstName)
    printChosenLine()
    theRating = askForRating()
    checkWhichPrize(theRating, totalPrice)
    printThankYouLine()
    #randombanner





if __name__ == '__main__':
    main()

