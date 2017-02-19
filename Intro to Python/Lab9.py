#!C:/python27/python.exe
'''
Kenneth Huynh N18178828
This program is for rec09.
'''
from __future__ import print_function

AVAILFOODS = [ "milk", "chocolate covered cherries", "apple", "orange", "banana", "corn on the cob", "kampyo sushi", "asparagus", "avacado", "alfalfa", "acorn squash", "almond package", "arugala bunch", "artichoke", "applesauce", "wasabi", "udon noodles", "tunafish can", "apple juice", "avocado sushi", "bruscetta", "bagel", "barley", "bisque", "bluefish", "bread", "broccoli", "buritto", "babaganoosh", "cabbage", "chocolate cake", "red velvet cake", "strawberry short cake", "carrots", "celery", "cheese", "catfish", "chowder", "clams", "coffee", "corn", "crab", "curry", "cereal", "chimichanga", "dumpling", "donut", "egg", "enchilada", "eggroll", "english muffin", "edimame", "eelSushi", "o toro sashimi", "fajita", "falafel", "fondu", "french toast", "french dip", "garlic", "ginger", "gnocchi", "granola", "grape", "green bean", "guacamole", "gumbo", "grits", "graham crackers", "halibut", "honey", "huenos rancheros", "hash browns", "hummus", "chocolate ice cream", "strawberry ice cream", "cherry garcia ice cream", "puri", "veggie kurma", "jambalaya", "kale", "ketchup", "kiwi", "kidney beans pckg", "great northern beans pckg", "lobster", "linguine", "lasagna", "pepperoni pizza", "mushroom pizza", "pancakes", "quesadilla", "quiche", "spinach", "spaghetti", "tater tots", "toast", "waffles", "walnuts", "peanuts", "hazelnuts", "cranberries", "yogurt", "ziti", "zucchini", "canteloupe", "figs", "salt", "pepper", "nutmeg", "yucca", "shichimi" ] 
FINISH = 'finish'
SHOP = 'shop'

# PART ONE

def makeDontBuy():
    '''returns the do not buy list'''
    dontBuy = []
    food = raw_input('Enter the food you do not want to buy: ').lower()
    while food != FINISH:
        if food in AVAILFOODS and food not in dontBuy:
            dontBuy.append(food)
        elif food not in AVAILFOODS:
            print('That food is not in the available list!!!')
        else: #can put in dont buy list
            print('Keep going')
        food = raw_input('Enter the food you do not want to buy: ').lower()
    return dontBuy

def makeBuy(dontBuy):
    '''returns the buy list'''
    doBuy = []
    food = raw_input('Enter the food you do want to buy: ').lower()
    while food != SHOP:
        if food in AVAILFOODS and food not in dontBuy:
            doBuy.append(food)
        elif food in dontBuy:
            print('''Sorry, it's in the don't buy list!''')
        else: #not available
            print('''They don't sell this!!!''')
        food = raw_input('Enter the food you do want to buy: ').lower()
    return doBuy

def printFoodsToBuy(doBuy):
    '''prints the list of foods to buy'''
    print (doBuy)

##def main():
##    dontBuy = makeDontBuy()
##    doBuy = makeBuy(dontBuy)
##    printFoodsToBuy(doBuy)
###########################################################

# PART TWO

##def countEachFood(doBuy):
##    '''counts the number of each food in the given list and returns a list of lists'''
##    newList = []
##    while len(doBuy) > 0:
##        foodFirst = doBuy[0]
##        numFirst = doBuy.count(doBuy[0])
##        for var in range(numFirst):
##            doBuy.remove(doBuy[0])
##        newList.append([foodFirst, numFirst])
##    print(newList)

def printListHead():
    '''prints the list heading'''
    print ('-- FAMILY SHOPPING LIST --')
    print ('FOOD      QUANTITY TO BUY')
    print ('--------------------------')

def createWholeList(doBuy):
    '''creates a whole list with the food followed by the number'''
    foodList = []
    quantList = []
    wholeList = []
    for food in doBuy:
        if food not in foodList:
            quantList.append(doBuy.count(food))
            foodList.append(food)
    for food in range(len(quantList)):
        wholeList.append([foodList[food], quantList[food]])
    wholeList.sort()
    return wholeList

def printList(wholeList):
    for food in wholeList:
        print('%s %i' % (food[0], food[1]))
        #print('s' if food[1] > 1 else '')
        
##def main():
##    dontBuy = makeDontBuy()
##    doBuy = makeBuy(dontBuy)
##    wholeList = createWholeList(doBuy)
##    printListHead()
##    printList(wholeList)

######################################################
# PART THREE

def askUser():
    userNum = int(raw_input('Enter 1 for add food to the shopping list.\nEnter 2 to create dont buy list.\nEnter 3 to display alphabetical list of all available foods.\nEnter 4 to quit and print shopping list.\nPLEASE DO 2 FIRST IF THIS IS YOUR FIRST TIME!!!'))
    return userNum

def main():
    while True:
        userNum = askUser()
        if userNum == 1:
            doBuy = makeBuy(dontBuy)
        elif userNum == 2:
            dontBuy = makeDontBuy()
        elif userNum == 3:
            AVAILFOODS.sort()
            print(AVAILFOODS)
        elif userNum == 4:
            wholeList = createWholeList(doBuy)
            printListHead()
            printList(wholeList)


if __name__ == '__main__':
    main()
