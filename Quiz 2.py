## Name: Tristan Ang

import random
from geometric_figures import *

'''Appendix'''

"""
Author: Danny Krizanc
Date: Oct 2106
This file contains a skeleton
implementation of geometric
figures including circles, triangles, rectangles and squares. Methods
available for each include those for computing the perimeter and area.
They all inherit from the class Figure which has one method for comparing figures
by their area.
The Point class is provided to be used by the other classes.
"""

'''Q1'''
##a
from math import modf
toople = modf(3.5)

##b
from itertools import count
'''for x in count(2,2): print x'''
'''for x in itertools.count(2,2): print x'''

##c
import calendar
## print calendar.isleap(2100)
## print isleap(2100)

'''Q2'''
class Diamond(Figure):
    
    '''Class Circle implements a circle given its center, a Point, and its
       radius, a float or int. Subclass of Figure.''' 

    def __init__(self,center,radius):
        
                
        self.center = center
        self.radius = radius
        self.side = sqrt(2)*radius

    def __str__(self):

        '''To string method for printing a circle'''

        return 'Diamond with center'+str(self.center)+' and radius '+str(self.radius)+''

    def __repr__(self):
        '''Representation of circle'''

        return 'Diamond('+repr(self.center)+','+repr(self.radius)+')'

##    def set_radius(self,r):
##        self.radius = r
##
##    def set_center(self,p):
##        self.center = p
##
##    def get_radius(self):
##        return self.radius
##
##    def get_center(self):
##        return self.center
##
##    def diameter(self):
##
##        '''Returns the diameter of circle'''
##        
##        return 2*self.radius

    def perimeter(self):

        '''Returns the perimeter of circle'''
        
        return 4*self.side
    
    def area(self):

        '''Returns the area of circle'''
        
        return self.side*self.side

def random_Diamond():
    radius = random.randint(1,50)
    center_x = random.randint(radius,100-radius)
    center_y = random.randint(radius,100-radius)
    center = center_x,center_y
    return Diamond(Point(center_x,center_y),radius)

def main_problem2():
    lst = []
    for i in range(5):
        lst.append(random_Diamond())
    lst.sort()
    for diamond in lst:
        print diamond, diamond.area()

'''Q3'''
def two_nines(n):
    digits = str(n)
    if digits.count('9') == 2:
        return True
    else:
        return False

def test_q3():
    assert not two_nines(0)
    assert not two_nines(1)
    assert two_nines(99)
    assert not two_nines(999)
    assert not two_nines(9)
    assert not two_nines(9341341324123432941324231423193412343124231)
    assert two_nines(93412432141234312431294314213423143)
    r1 = random.randint(0,100)
    r2 = random.randint(0,100)
    r3 = random.randint(0,100)
    test1 = int(r1*'1'+'9'+r2*'2'+'9'+r3*'3')
    print 'Passed all tests'

'''Q4'''

def triangle_area():
    from math import sqrt
    a,b,c = input('Please input the length of the sides of triangle a,b,c: ')
    while True:
        s = (a+b+c)/2.
        try:
            area = sqrt(s*(s-a)*(s-b)*(s-c))
            print 'The area of the triangle is',area
            break
        except ValueError:
            a,b,c = input('Invalid inpue, please input lengths a,b,c again: ')
            continue
    
        
        
    

