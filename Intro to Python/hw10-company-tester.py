'''
cs1114 

Submission: hw10 tester code

Programmer: Kenneth Huynh
Username: kh1983

Purpose of program, assumptions, constraints:

This program is for hw10 tester code.
This is the tester code for hw10.
'''

from hw10 import *

def main():
    company1 = Company('Elephant')
    company1.hireWorker(2342, 'sally', 26.40)
    company1.hireWorker(5343, 'joe', 34.60)
    company1.addHours(2342, 5)
    company1.addHours(5343, 6)
    company1.payAll()
    company1.fireWorker(5343)
    company1.hireWorker(1234, 'ralph', 20.64)
    company1.changeHourly(1234, 22.60)
    company1.addHours(1234, 8)
    company1.addHours(2342, 7)
    company1.payAll()

if __name__ == '__main__':
    main()
