## Tristan Ang Tze Heng

import geometric_figures

## import did not work so geometric_figures.py pasted here##
from math import sqrt,pi
    
class Point(object):
    
    '''Class Point implements a point on the Cartesian plane (x,y) using
       two instance variables x and y indicating their co-ordinates'''
    
    def __init__(self,x=0,y=0):
        '''Constructor for Point defaults to (0,0)'''
        self.x = x
        self.y = y
        
    def __str__(self):
        
        '''To string method for printing of a Point as a tuple'''
        
        return '('+str(self.x)+','+str(self.y)+')'

    def __repr__(self):
        '''Representation of Point'''

        return 'Point('+str(self.x)+','+str(self.y)+')'
    
    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def setx(self,x):
        self.x = x

    def sety(self,y):
        self.y = y
        
    def distance_to(self,point):

        '''Computes the distance between self and point'''
        
        return sqrt((self.x-point.x)**2+(self.y-point.y)**2)

class Figure(object):
    '''Super class Figure of Circle, Rectangle, Square. Implements
       __cmp__(self,other) ordering by area.'''

    def __cmp__(self,other):

        '''Returns comparison of self area and other area'''

        if self.area()>other.area():
            return 1
        elif self.area()==other.area():
            return 0
        else:
            return -1

'''Q1'''
##a
import cmath
x = 10+4j
y = cmath.sin(x)
print y.real

##b
import itertools
lst = list(itertools.permutations([1,2,3]))
lst = [list(lst[i]) for i in range(len(lst))]
print lst

##c
import calendar
print calendar.leapdays(1899,2001)

'''Q2'''
class Annulus(Figure):

    def __init__(self,p,r1,r2):

        self.center = p
        self.innerradius = r1
        self.outerradius = r2

    def __str__(self):

        return 'Annulus with center'+str(self.center)+', inner radius '+str(self.innerradius)+', and outer radius '+str(self.outerradius)+''

    def __repr__(self):
       
        return 'Annulus('+repr(self.center)+','+repr(self.innerradius)+','+repr(self.outerradius)+')'

    def set_center(self,p):
        self.center = p

    def get_center(self):
        return self.center

    def perimeter(self):
        
        return 2*pi*(self.innerradius+self.outerradius)
    
    def area(self):

        '''Returns the area of circle'''
        
        return pi*(self.outerradius**2-self.innerradius**2)
    
import random

def random_Annulus():
    '''Returns a random Annulus that fits on 100 by 100 grid'''

    outerradius = random.randint(2,50)
    innerradius = random.randint(1,(outerradius-1))
    center_x = random.randint(outerradius,100-outerradius)
    center_y = random.randint(outerradius,100-outerradius)
    assert outerradius+center_y <= 100 and outerradius-center_y <= 100 and outerradius+center_x <= 100 and outerradius-center_x <= 100
    return Annulus(Point(center_x,center_y),innerradius,outerradius)

##def test_randa():
##    for i in range(100):
##        x = random_Annulus()
##        print x
##    print 'passed'

def main_problem2():

    lst = []
    for i in range(5):
        lst.append(random_Annulus())
    lst.sort()
    for annulus in lst:
        print annulus,annulus.area()

'''Q3'''
def perfect_number(x):
    ## if x%2 !=0:  '''it is unknown if there is any odd perfect number'''
    ##     return False
    summation = 1
    if x==1:
        return False
    for i in range(2,int(sqrt(x)+1)):
        if x % i ==0:
            summation += i
            summation += x/i
    if summation == x:
        return True
    else:
        return False
    
def perfect_test():
    for i in range(1,6):
        assert not perfect_number(i)
    for i in range(7,28):
        assert not perfect_number(i)
    assert perfect_number(6)
    assert perfect_number(28)
    p = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253, 4423, 9689, 9941, 11213, 19937, 21701, 23209, 44497, 86243, 110503, 132049, 216091, 756839, 859433, 1257787, 1398269, 2976221, 3021377, 6972593, 13466917, 20996011, 24036583, 25964951, 30402457,32582657]
    for i in range(7):
        number = (2**(p[i]-1))*((2**p[i])-1)
        assert perfect_number(number)
    for i in range(100):
        multiplier = random.randint(1,100)
        oddnumber = 2*multiplier-1
        assert not perfect_number(oddnumber)
    print 'Passed all tests'
    
perfect_test()

'''Q4'''
def newton():
    force = int(raw_input('Please input the force applied: '))
    mass = int(raw_input('Please input the mass of object: '))
    done = False
    while not done:
        try:
            while mass < 0:
                mass = int(raw_input('No Negative mass, reinput: '))
            acceleration = 1.*force/mass
        except ZeroDivisionError:
            mass = int(raw_input('No zero mass, reinput: '))
            continue
        print 'The acceleration of the object is',acceleration
        done = True
    
