#COMP 211 - Fall 2016 - Lab 2 solutions
#Author: Danny Krizanc
#Date: Sept, 2016

#Problem 1

def f1(a,b=4,c=5):
    print a,b,c

f1(1,2)

def f2(a,b,c=5):
    print a,b,c 

f2(1,c=3,b=2)

x = 3
def f3():
    x = 4
f3()
print x

x = 3
def f4():
    x = 4
    print x
f4()
print x

x = 3
def f5():
    global x
    x = 4
f5()
print x

def f(x):
    def g():
        x = 'abc'
        print 'x = ',x
    def h():
        z = x
        print 'z = ',z
    x = x + 1
    h()
    g()
    print 'x = ',x
    return g
x = 3
z = f(3)
print 'x = ',x
print 'z = ',z
z()



#Problem 2

#(a)
def perfect_square(x):
    '''Returns True iff x is a perfect square'''
    return type(x) == int and x >= 0 and x == (int(x**.5)**2)

#Another solution using built-in Python is_integer() function
def perfect_square2(x):
    '''Returns True iff x is a perfect square'''
    return type(x) == int and x >= 0 and (x**.5).is_integer()

#(b)
def hundreds_digit(x):
    '''Returns the hundreds digit of x; if abs(x) < 100 returns 0'''
    if type(x) != int or abs(x)<100:
        return 0
    else:
        return int(str(x)[-3])

#(c)
def in_circle(x,y,r=1,x0=0,y0=0):
    '''Returns True iff (x,y) lies on or inside the circle of radius
       r centered at (x0,y0). Defaults to circle of radius 1
       centered at (0,0).'''
    return ((x-x0)**2 + (y-y0)**2) < r**2 #no need to take sqrt
    
#(d) 
def day_of_week(day,month,year=None):
    '''Uses Zeller's formula to compute the day of the week of
       a given date DD/MM/YYYY -> day/month/year. The result is
       given by the correspondence Saturday = 0, ..., Friday = 6.
       The default value for the year is the current year.'''
    if not year:
        import datetime
        year = datetime.date.today().year #today's year from datetime module
    if month < 3:
        month = month+12
        year = year-1
    year_of_century = year%100
    century = year/100
    day_week = (day + (13*(month+1))/5 + year_of_century
                 + year_of_century/4 + century/4
                 - 2*century)%7
    return day_week

#Another soln using date time

def day_of_week2(day,month,year=None):
    '''Computes the day of the week of a given day/month/year.
       The result is given by the correspondence Monday = 0, ...,
       Sunday = 6. The default value for the year is the current
       year. Raises an exception if day/month/year is not a valid
       date.'''
    
    import datetime
    if not year:
        year = datetime.date.today().year
    return datetime.date(year,month,day).weekday()

#If you want to return the actual day rather than number...

def day_of_week3(day,month,year=None):
    '''Returns the day of the week of a given day/month/year as a string.
       The default value for the year is the current
       year. Raises an exception if day/month/year is not a valid
       date.'''
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday',
            'Saturday','Sunday']
    import datetime
    if not year:
        year = datetime.date.today().year
    return days[datetime.date(year,month,day).weekday()]


#(e) Soln from wikipedia

def is_leap_year(year):
    '''Returns True iff year represents a leap year.'''
    
    if year%400 == 0:
        return True
    elif year%100 == 0:
        return False
    elif year%4 == 0:
        return True
    else:
        return False

#A slightly shorter soln?
    
def is_leap_year2(year):
    '''Returns True iff year represents a leap year'''
    if year%4 !=0:
        return False
    elif year%100 == 0 and year%400 != 0:
        return False
    else:
        return True


# Problem 3

#(a)
def double_factorial(n):
    '''Returns n!!'''

    if n == 0 or n == 1:
        return 1
    else:
        return n*double_factorial(n-2)


#(b)

def increment(lst):
    '''
       Args: lst - list of numbers
       Returns: a list of numbers consisting of each element in lst
       incremented by 1
    '''
    
    if lst == []:
        return []
    else:
        return [lst[0]+1] + increment(lst[1:])

#(c)

def palindrome(string):
    '''Returns true iff string is a palindrome'''

    if len(string) == 0 or len(string) == 1:
        return True
    else:
        if string[0] == string[-1]:
            return palindrome(string[1:-1])
        else:
            return False


#(d)

def remove_all(e,L):
    '''Remove all occurrences of e from L'''

    if L == []:
        return []
    elif e == L[0]:
        return remove_all(e,L[1:])
    else:
        return [L[0]]+remove_all(e,L[1:])



    
# Problem 4

def flatten(lst):
    '''Returns a 'flattened' version of lst as explained in lab handout'''
    
    if lst == []:
        return []
    elif type(lst[0]) == list:
        return flatten(lst[0])+flatten(lst[1:])
    else:
        return [lst[0]]+flatten(lst[1:])

#Problem 5



def subset_sum(n,lst):
    '''
       Args: n - an int
             lst - a list of ints
       Returns: True iff there is a sublist of the lst which adds to n
    '''
    if lst == []:
        return False
    elif lst[0] == n:
        return True
    else:
        return subset_sum(n,lst[1:]) or subset_sum(n-lst[0],lst[1:])

    why or?

   
