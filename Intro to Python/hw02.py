#!C:/python27/python.exe
''' 
cs1114 

Submission: hw02

Programmer: Kenneth Huynh
Username: kh1983

Purpose of program, assumptions, constraints:

This program shows the bridge brochure and pauses the screen.

'''
from __future__ import print_function
import bridgeBuilders

def showBridgeSalesBrochure():
    '''this functions shows the Bridge Sales Brochure'''
    print('Single Span, Light Roadway Bridge:\n')
    bridgeBuilders.showSingleLightRoadway()
    print('\nSingleSpan, Heavy Roadway Bridge:\n')
    bridgeBuilders.showSingleHeavyRoadway()
    print('\nDouble Span, Light Roadway Bridge:\n')
    bridgeBuilders.showDoubleLightRoadway()
    print('\nDouble Span, Heavy Roadway Bridge:\n')
    bridgeBuilders.showDoubleHeavyRoadway()

def pauseTheScreen():
    '''this function pauses the screen'''
    raw_input()
    
def main():
    showBridgeSalesBrochure()
    pauseTheScreen()
    
if __name__ == '__main__':
    main()
    
