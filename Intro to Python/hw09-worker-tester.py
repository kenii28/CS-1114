'''
cs1114 

Submission: hw09 tester code

Programmer: Kenneth Huynh
Username: kh1983

Purpose of program, assumptions, constraints:

This program is for hw09 tester code.
This is the tester code for hw09.
'''
from hw09_worker import WorkerRec


def main():
    a = WorkerRec('12345', 'Hi')
    print(a)
    a.changeTitle('Poop')
    print(a)
    a.addHours(4)
    print(a.getHours())
    print(a.getPaid())
    a.addHours(-3)
    print(a.getHours())
    b = WorkerRec('23412', 'God', 20.35)
    print(b)
    b.changeHourly(20.50)
    print(b)

if __name__ == '__main__':
    main()

