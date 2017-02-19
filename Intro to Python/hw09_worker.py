'''
cs1114 

Submission: hw09

Programmer: Kenneth Huynh
Username: kh1983

Purpose of program, assumptions, constraints:

This program is for hw09.
This is the class definition for hw09.
'''

ADD_NEG_HOURS_ERROR = 0
LESS_THAN_MIN_HOURLY = 1

class WorkerRec( object ):
    '''
        name
        ssn
        hourly wage
        hours worked
        title
        __str__ formatted:
                title name [ssn]: $hourly
    '''
    def __init__(self, ssn, name, hourly = 17.22, hours = 0):
        '''
            data members    assumptions:
                ssn            ssn is of correct form
                name           name is a str
                hourly         hourly is float
                title          title is str
        '''
        self.__ssn = ssn
        self.__name = name
        self.__hourly = hourly
        self.__hours = hours
        self.__title = ''

    def changeTitle(self, newTitle):
        '''change someone's title, needs their ssn'''
        self.__title = newTitle

    def changeHourly(self, newHourly):
        '''changes the hourly rate of the worker'''
        if newHourly <= 17.22:
            return LESS_THAN_MIN_HOURLY
        self.__hourly = newHourly

    def getHourly(self):
        '''returns the hourly of the worker'''
        return self.__hourly

    def addHours(self, numHours):
        '''adds hours to the number of hours the worker worked.
            returns ADD_NEG_HOURS_ERROR if a negative amount of hours
            is entered.
        '''
        if numHours <= 0:
            return ADD_NEG_HOURS_ERROR
        else:
            self.__hours += numHours

    def getHours(self):
        '''returns the number of hours worked'''
        return self.__hours

    def getSSN(self):
        '''returns the ssn of the worker'''
        return self.__ssn
    
    def getTitle(self):
        '''returns the title of the worker'''
        return self.__title

    def getName(self):
        '''returns the name of the worker'''
        return self.__name
    
    def getPaid(self):
        '''returns the amount the worker gets paid'''
        pay = self.__hourly * self.__hours
        return pay
        
    def __str__(self):
        '''returns worker rec in the form of:
            title name [ssn]: $hourly
        '''
        return '%s %s [%s]: $%.2f per hour' % (self.__title, self.__name, self.__ssn, self.__hourly)
    
