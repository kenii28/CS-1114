#!C:/python27/python.exe
'''
Kenneth Huynh
This program prints a receipt from the COFFEE AND DOUGHNUT SHOPPE.
'''
from __future__ import print_function
import Lab4

costOneDoughnut = .64
costOneCoffee = .77
taxRate = 0.0846

def drawSlashBackSlashLine():
    '''draws /\ 15 times'''
    slashBackSlash = "/\\" * 15
    print(slashBackSlash)
    
def drawBackSlashSlashLine():
    '''draws \/ 15 times'''
    BackSlashSlash = "\\/" * 15
    print(BackSlashSlash)

def writeShoppeName():
    '''prints the name of the shoppe'''
    print('THE COFFEE AND DOUGHNUT SHOPPE')

def getNumber():
    numOfCoffee = float(raw_input('Enter the number of cups of coffee: '))
    numOfDoughnut = float(raw_input('Enter the number of doughtnuts: '))
    return numOfCoffee, numOfDoughnut

def calcCostCoffee(numOfCoffee):
    costCoffee = numOfCoffee * costOneCoffee
    return costCoffee

def calcCostDoughnut(numOfDoughnut):
    costDoughnut = numOfDoughnut * costOneDoughnut
    return costDoughnut

def calcCostBeforeTax(costCoffee, costDoughnut):
    costBeforeTax = costCoffee + costDoughnut
    return costBeforeTax

def calcTax(costBeforeTax):
    costTax = costBeforeTax * taxRate
    return costTax

def calcAmountOwed(costBeforeTax, costTax):
    amountOwed = costBeforeTax + costTax
    return amountOwed
    
def writeThankYou():
    print("Thank you for buying local.")

def showBill(numOfCoffee, numOfDoughnut, costCoffee, costDoughnut, costBeforeTax, costTax, amountOwed):
    print("\n\n")
    drawSlashBackSlashLine()
    writeShoppeName()
    drawBackSlashSlashLine()
    print("\n")
    print("%.1f cups of coffee: $%.2f" % (numOfCoffee, costCoffee))
    print("    %.1f doughnuts: $%.2f" % (numOfDoughnut, costDoughnut))
    print("\t        tax: $%.2f" % (costTax))
    print("\n")
    print("      Amount Owed: $%.2f" % (amountOwed))
    print("\n")
    writeThankYou()
    
def main():
    numOfCoffee, numOfDoughnut = getNumber()
    costCoffee = calcCostCoffee(numOfCoffee)
    costDoughnut = calcCostDoughnut(numOfDoughnut)
    costBeforeTax = calcCostBeforeTax(costCoffee, costDoughnut)
    costTax = calcTax(costBeforeTax)
    amountOwed = calcAmountOwed(costBeforeTax, costTax)
    showBill(numOfCoffee, numOfDoughnut, costCoffee, costDoughnut, costBeforeTax, costTax, amountOwed)    
    Lab4.printAsCoins(amountOwed)
    
if __name__ == '__main__':
    main()

