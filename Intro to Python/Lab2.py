#!C:/python27/python.exe
'''
Kenneth Huynh
This program puts the name joe in a box with x borders with a Welcome message
and a Thank You message.
'''
from __future__ import print_function
import os

def writeWelcome():
    '''Writes Welcome'''
    print("Welcome")

def writeThankYou():
    '''Writes Thank You'''
    print("Thank you")

def drawXLine():
    '''Draws a line of X'''
    print("XXXXXXX")

def drawSpaceLine():
    '''Draws a space line with an X in the beginning and end'''
    print("X     X")
    
def drawNameLine():
    '''Draws a line with joe in it and X in the beginning and end'''
    print("X joe X")

def main():
    writeWelcome()
    drawXLine()
    drawSpaceLine()
    drawNameLine()
    drawSpaceLine()
    drawXLine()
    writeThankYou()
    os.system("pause")

if __name__ == '__main__':
    main()
