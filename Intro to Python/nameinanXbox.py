#!C:/python27/python.exe
'''
Kenneth Huynh
This program puts a name into a box surrounded by Xs.
'''
from __future__ import print_function

def drawXLine(name):
    '''Draws a line of X'''
    print(len(name) * "X")

def drawSpaceXLine(name):
    '''Draws a space line with an X in the beginning and end'''
    print("X", (len(name)+2)*" ","X")
    
def drawNameLine(name):
    '''Draws a line with the name in it and X and space in the beginning and end'''
    print("X", name, "X")

def drawBoxWithName(name):
    '''Draws a box with a name inside of an X border'''
    drawXLine()
    drawSpaceXLine()
    drawNameLine()
    drawSpaceXLine()
    drawXLine()
    
def main():
    drawBoxWithName(name)
    
    
if __name__ == '__main__':
    main()
