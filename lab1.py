#COMP 211 - Spring 2016 - Lab 1 solutions
#Author: Danny Krizanc
#Date: Sept, 2016


#Problem 2
word = 'danny'
print word.capitalize(),word.upper(),word.count('a')

#Problem 3

string = 'abc'
rev_string = string[::-1] # rev_string = reverse(string)
print string,rev_string
lst = [1,2,3]
rev_lst = lst[::-1] #rev_lst = reverse(lst)
print lst, rev_lst
lst.reverse() #reverses string in place
print lst
rev_string2 = ''.join(reversed(string)) # reversed returns iterator of reverse
                                        # of sequence
print string, rev_string2

#Problem 4: Mystery functions f and g
                                        
def first_digit(x):
    '''
    Args: int x
    Returns: int, the first digit of x
    '''
    y = str(x)
    return int(y[0])

print 'First digit of 327 is: ', first_digit(327)

def sum_1_to_n(n):
    '''
    Args: int n>0
    Returns: sum from 1 to n
    '''
    return n*(n+1)/2

print "Sum from 1 to 10 equals ", sum_1_to_n(10)

def is_digit(x):
    '''
    Args: int x
    Returns: True iff x is a single decimal digit value
    '''
    return type(x) == int and x == x%10

print is_digit(5) # returns True
print is_digit('5') # returns False
print is_digit(55) # returns False


#Problem 5

def full_rect(a,b):
    '''
    Prints a rectangle of *'s of width a and height b
    
    Args: int a
          int b
          
    Returns: None
    '''
    
    print b*(a*'*' + '\n')

full_rect(4,5)


#Problem 6

def line_default(a,b=1):
    '''
    Prints a rectangle of *'s of width a and height b; b defaults to 1
    
    Args: int a
          int b
          
    Returns: None
    '''
    
    print b*(a*'*' + '\n')

line_default(10)

#Problem 7

def area_of_triangle(a,b,c):
    '''
    Args: Numeric a,b,c
    
    Returns: Area of triangle with side lengths a, b, c
    '''

    from math import sqrt
    p = (a+b+c)/2.0
    return sqrt(p*(p-a)*(p-b)*(p-c))

print area_of_triangle(1,1,1)
print area_of_triangle(3,4,5)
print area_of_triangle(1,1,3)







