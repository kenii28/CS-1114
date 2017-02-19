'''
cs1114 

Submission: hw10

Programmer: Kenneth Huynh
Username: kh1983

Purpose of program, assumptions, constraints:

This program is for hw10.
This is the company class for hw10.
'''

from hw09_worker import WorkerRec
from hw09_worker import ADD_NEG_HOURS_ERROR
from hw09_worker import LESS_THAN_MIN_HOURLY

DUPLICATE_SSN = 98989
NO_SSN = 2342

class Company(object):
    '''
        creates a company that handles workers

        contains:
            name
            dictionary of workers using ssn
         accessing workers allows:
            changeTitle(newTitle)
            changeHourly(newHourly)
            getHourly()
            addHours(numHours)
            getHours()
            getSSN()
            getTitle()
            getName()
            getPaid()
    '''
    def __init__(self, name):
        '''
            fields         type
            name            str
            records         dictionary

        '''
        self.__name = name
        self.__records = {}

    def __getName(self):
        '''returns the name of the company'''
        return self.__name

    def changeName(self, newName):
        '''changes the name of the company'''
        self.__name = newName

    def __verifyssn(self, ssn):
        '''verifies if the ssn has been used.
            returns True is ssn is in dictionary.
            False otherwise'''
        return ssn in self.__records
    
        
    def hireWorker(self, ssn, name, hourly = 17.22, hours = 0):
        '''adds worker to the dictionary. return DUPLICATE_SSN if there is a
            duplicate ssn'''
        if self.__verifyssn(ssn):
            return DUPLICATE_SSN
        wr = WorkerRec(ssn, name, hourly, hours)
        self.__records[ssn] = wr
        
    def addHours(self, ssn, numHours):
        '''adds hours to worker record. if negative or zero hours returns
            ADD_NEG_HOURS_ERROR
            returns NO_SSN if ssn does not exist'''
        if not self.__verifyssn(ssn):
            return NO_SSN
        theHours = self.__records[ssn].addHours(numHours)
        if theHours == ADD_NEG_HOURS_ERROR:
            return ADD_NEG_HOURS_ERROR

    def changeHourly(self, ssn, newHourly):
        '''changes the hourly pay for worker.
            returns NO_SSN if ssn does not exist
            returns LESS_THAN_MIN_HOURLY if hourly is less than 17.22
        '''
        if not self.__verifyssn(ssn):
            return NO_SSN
        theHourly = self.__records[ssn].changeHourly(newHourly)
        if theHourly == LESS_THAN_MIN_HOURLY:
            return LESS_THAN_MIN_HOURLY

    def changeTitle(self, ssn, newTitle):
        '''changes the title of worker
            returns NO_SSN if ssn does not exist
        '''
        if not self.__verifyssn(ssn):
            return NO_SSN
        theTitle = self.__records[ssn].changeTitle(newTitle)

    def payAll(self):
        '''writes to a file to be sent to the accounting department'''
        companyName = __getName()
        fileName = companyName + '.pay'
        self.__records.keys().sort()
        fh = open(fileName, 'w')
        for keys in self.__records.keys():
            ssn = self.__records.getSSN()
            name = self.__records.getName()
            hourly = self.__records.getHourly()
            hours = self.__records.getHours()
            title = self.__records.getTitle()
            amtOwed = hourly * float(hours)
            fh.write(ssn + '\n')
            fh.write(name, '$', amtOwed)
            if title != '':
                fh.write('[', title, ']\n')
            else: #no title
                fh.write('\n')
            self.__records[ssn].changeHours(0)
        fh.close()
        
    def fireWorker(self, ssn):
        '''fires a worker'''
        name = self.__records.getName()
        hourly = self.__records.getHourly()
        hours = self.__records.getHours()
        title = self.__records.getTitle()
        amtOwed = hourly * float(hours)
        fileName = name + '.FINAL.PAY'
        fh = open(fileName, 'w')
        fh.write(ssn + '\n')
        fh.write(name, '$', amtOwed)
        if title != '':
            fh.write('[', title, ']\n')
        else: #no title
            fh.write('\n')
        fh.close()
        self.__records.pop(ssn)
    
