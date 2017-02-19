'''
This is a module that deals with money!
'''

from __future__ import print_function


PESOS_PER_DOLLAR = 0.07
DOLLAR_AMOUNT = 1
quarterAmount = .25
dimeAmount = .10
nickelAmount = .05
pennyAmount = .01

def printAsUSDollars(theAmount):
    '''prints any given float amount in either the $999.99 or the USD 999.99 form'''
    userInput = raw_input('''Enter 1 if you want the value amount to have a USD in front of
    the value, otherwise it will start with $: ''')
    inUSDollars = round(theAmount, 2)
    print ("The amount of in US Dollars is: USD %.2f " % (inUSDollars)) if userInput == '1' else print ("The amount of in US Dollars is: $%.2f " % (inUSDollars))

def convertPesosToUSDollars(thePesoAmount):
    ''''returns the number of whole US dollars and any leftover amount'''
    theWholeUSDollars = int(thePesoAmount*PESOS_PER_DOLLAR)
    theLeftover = thePesoAmount - (theWholeUSDollars / PESOS_PER_DOLLAR)
    theLeftoverPesos = round(theLeftover, 2)
    return (theWholeUSDollars, theLeftoverPesos)
    
def printAsCoins(theAmount):
    '''given the amount of money in US Dollars, prints the number of coins of each
    denomination there would be if it was in coins.'''
    numDollarCoins = theAmount//DOLLAR_AMOUNT
    theLeftover = theAmount%numDollarCoins
    numQuarters = (theLeftover // quarterAmount)
    theLeftover = theLeftover%quarterAmount
    numDimes = (theLeftover // dimeAmount)
    theLeftover = theLeftover%dimeAmount
    numNickels = (theLeftover // nickelAmount)
    theLeftover = theLeftover%nickelAmount
    numPennies = (theLeftover // pennyAmount)
    if numDollarCoins > 0:
        if numDollarCoins > 1:
            print('%i dollar coins' % (int(numDollarCoins)))
        else:
            print('%i dollar coin' % (int(numDollarCoins)))
    if numQuarters > 0:
        if numQuarters > 1:
            print('%i quarters' % (int(numQuarters)))
        else:
            print('%i quarter' % (int(numQuarters)))
    if numDimes > 0:
        if numDimes > 1:
            print('%i nickels' % (int(numDimes)))
        else:
            print('%i nickel' % (int(numDimes)))
    if numNickels > 0:
        if numNickels > 1:
            print('%i dimes' % (int(numNickels)))
        else:
            print('%i dime' % (int(numNickels)))
    if numPennies > 0:
        if numPennies > 1: 
            print('%i pennies' % (int(numPennies)))
        else:
            print('%i penny' % (int(numPennies)))
    #print ('''Number of dollar coins: %i\nNumber of quarters: %i\nNumber of dimes: %i\nNumber of nickels: %i\nNumber of pennies: %i''' % (numDollarCoins, numQuarters, numDimes, numNickels, numPennies))

def quantityOfCoins(theAmount):
    '''given the amount of money in US Dollars, prints the total number of coins there would be if
    it was in coins'''
    numDollarCoins = theAmount//DOLLAR_AMOUNT
    theLeftover = theAmount%numDollarCoins
    numQuarters = (theLeftover // quarterAmount)
    theLeftover = theLeftover%quarterAmount
    numDimes = (theLeftover // dimeAmount)
    theLeftover = theLeftover%dimeAmount
    numNickels = (theLeftover // nickelAmount)
    theLeftover = theLeftover%nickelAmount
    numPennies = (theLeftover // pennyAmount)
    totalCoins = numDollarCoins + numQuarters + numDimes + numNickels + numPennies
    return totalCoins
    
