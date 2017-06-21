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


class Circle(Figure):
    
    '''Class Circle implements a circle given its center, a Point, and its
       radius, a float or int. Subclass of Figure.''' 

    def __init__(self,p,r):
        
        '''Constructor for Circle takes a Point p and radius r'''
        
        self.center = p
        self.radius = r

    def __str__(self):

        '''To string method for printing a circle'''

        return 'Circle with center'+str(self.center)+' and radius '+str(self.radius)+''

    def __repr__(self):
        '''Representation of circle'''

        return 'Circle('+repr(self.center)+','+repr(self.radius)+')'

    def set_radius(self,r):
        self.radius = r

    def set_center(self,p):
        self.center = p

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.center

    def diameter(self):

        '''Returns the diameter of circle'''
        
        return 2*self.radius

    def perimeter(self):

        '''Returns the perimeter of circle'''
        
        return 2*pi*self.radius
    
    def area(self):

        '''Returns the area of circle'''
        
        return pi*self.radius**2


class Triangle(Figure):
    '''Class Triangle implements a triangle represented by its three corners.
       Subclass of Figure.'''

    def __init__(self,p1,p2,p3):
        '''Constructor for a Triangle'''

        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __str__(self):
        '''To string method for Triangle'''

        return 'Triangle with corners '+str(self.p1)+','+str(self.p2)+','+str(self.p3)+''
    def __repr__(self):
        '''Representation of circle'''

        return 'Triangle('+repr(self.p1)+','+repr(self.p2)+','+repr(self.p3)+')'

    def perimeter(self):
        '''Returns the perimeter of triangle'''

        return (self.p1.distance_to(self.p2)+
                self.p2.distance_to(self.p3)+
                self.p3.distance_to(self.p1))

    def area(self):
        '''Returns the area of triangle using Heron's formula'''

        s1 = self.p1.distance_to(self.p2)
        s2 = self.p2.distance_to(self.p3)
        s3 = self.p3.distance_to(self.p1)
        s = (s1+s2+s3)/2.0
        return sqrt(s*(s-s1)*(s-s2)*(s-s3))

class Rectangle(Figure):

    def __init__(self,l,h,x=0,y=0):

        self.o = (x,y)
        self.h = h
        self.l = l
        self.tl = (x,y+h)
        self.tr = (x+l,y+h)
        self.br = (x+l,y)
        
    def __str__(self):
 
        return 'Rectangle with vertices '+str(self.o)+','+str(self.tl)+','+str(self.tr)+','+str(self.br)+''

    def __repr__(self):

        return 'Rectangle('+repr(self.l)+','+repr(self.h)+','+repr(self.o[0])+','+repr(self.o[1])+')'

##    def perimeter(self):
##        '''Returns the perimeter of triangle'''
##
##        return (self.p1.distance_to(self.p2)+
##                self.p2.distance_to(self.p3)+
##                self.p3.distance_to(self.p1))
##
##    def area(self):
##        '''Returns the area of triangle using Heron's formula'''
##
##        s1 = self.p1.distance_to(self.p2)
##        s2 = self.p2.distance_to(self.p3)
##        s3 = self.p3.distance_to(self.p1)
##        s = (s1+s2+s3)/2.0
##        return sqrt(s*(s-s1)*(s-s2)*(s-s3))


'''Create some figures and sort by area'''

x = Point()
y = Point(3,0)
z = Point(0,4)
t1 = Triangle(x,y,z)

y = Point(8,0)
z = Point(4,3)
t2 = Triangle(x,y,z)

c1 = Circle(x,sqrt(2.0))
c2 = Circle(y,5)

L = [c1,c2,t2,t1]

print L
L.sort()
print L
    


    

    

        
        
    
    
    


    
