from __future__ import print_function
import random

def drawWeirdString( first, second ):
    ''' draw a string that is the string made of the value of first raised to
        the power of second repeated second rasied to the power of irst
        times.
        E.g.: If the calls passes in 2 and 3, the string will be: '888888888\n'
        2^3 is 8 and 3^2 is 9 so there are 9 '8' characters drawn
    '''
    firstInt = int(first)
    secondInt = int(second)
    first = str(firstInt**secondInt)
    second = secondInt**firstInt
    print(first*second)

def drawRandMultiples(first,second,third):
    firstRand = random.randint(3,17)
    secondRand = random.randint(5,22)
    thirdRand = random.randint(2,14)
    print(first*firstRand, second*secondRand, third*thirdRand, sep == '')
