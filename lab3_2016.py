# Solutions to COMP 211 Lab 3
# Author: Danny Krizanc
# Date: Sept 2016

# Problem 1a

def first_n_cubes_for(n):
    '''Returns a list of the first n cubes (starting with 1)
       using for loop'''
    
    cubes = []
    for i in range(1,n+1):
        cubes.append(i**3)
    return squares

def first_n_cubes_while(n):
    '''Returns a list of the first n cubes (starting with 1)
       using while loop'''

    cubes = []
    i = 1
    while i<=n:
        cubes.append(i**3)
        i = i + 1
    return cubes

# Problem 1b

def cubes_less_than_for(n):
    '''Returns a list of all cubes less than n
       using for loop'''
    
    cubes = []
    end = int(n**(1.0/3))
    for i in range(1,end+1):
        cubes.append(i**3)
    return cubes

def cubes_less_than_while(n):
    '''Returns a list of all cubes less than n
       using while loop'''
    
    cubes = []
    i = 1
    while i**3 <= n:
        cubes.append(i**3)
        i = i + 1
    return cubes

#I think the first problem is easier with a for loop and the second
#problem is easier with a while loop. In general it might be difficult
#to figure out where to stop in the second problem for some functions.
#Using a while eliminates the need to figure it out. One could use a
#break statement but that seems a little more confusing than a while.

# Problem 2

def num_vowels(word):
    '''The number of vowels (aeiou) in word is returned.'''

    word = word.lower() # Make all characters lower case
    cnt = 0
    for char in word:
        if char in 'aeiou': #Simpler than char == 'a' or etc. 
            cnt = cnt + 1
    return cnt

# Problem 3

def avg_vowels():
    '''User enters words and the average number of vowels in
       the words entered is printed'''

    word = raw_input('Enter a word or press Return to quit: ')
    words = 0.0
    vowels = 0.0
    while word != '':
        words = words + 1
        vowels = vowels + num_vowels(word)
        word = raw_input('Enter a word or press Return to quit: ')
    if words != 0.0: # Check for case of no words input
        avg = vowels/words
    else:
        avg = 0.0
    print "The average number of vowels was", str(avg)+'.'

# Problem 4

import random

def roll_dice():
    '''Returns the sum of two random die'''
    
    return random.randint(1,6)+random.randint(1,6)

def craps_round():
    '''Plays a single round of craps - usual rules'''

    roll = roll_dice()
    print "You rolled", roll
    if roll == 2 or roll == 3 or roll == 12:
        print "Craps, you lose."
    elif roll == 7 or roll == 11:
        print "You win!"
    else:
        next_roll = roll_dice()
        print "Your next roll is", next_roll
        while next_roll != roll and next_roll != 7:
            next_roll = roll_dice()
            print "Your next roll is", next_roll
        if next_roll == roll:
            print "You win!"
        else:
            print "You lose."

def craps():
    '''Plays craps until user doesn't want to play anymore'''

    play = raw_input("Do you want to play (y or n)? ")
    while play == 'y':
        craps_round()
        play = raw_input("Play again (y or n)? ")
    print "Goodbye"

#Problem 5
    
def triangle(n,direction='up'):
    '''Print an up or down triangle of height n'''
    
    rows = [i*'*'for i in range(1,n+1)]
    if direction=='down': rows.reverse()
    for x in rows:
        print x

#Problem 6

#(a)
        
def double_factorial(n):
    '''Returns n!! equal to 1 if n = 0 or n = 1; n*(n-2)!! otherwise'''
    
    if n==0 or n==1:
        return 1
    if n%2==0:
        start = 2
    else:
        start = 1
    prod = 1
    for i in range(start,n+1,2):
        prod = prod*i
    return prod

#Personally I think this is a place where recursion makes sense. Its
#certainly shorter. 

def double_factorial_rec(n):
    '''Returns n!! equal to 1 if n = 0 or n = 1; n*(n-2)!! otherwise'''

    if n==0 or n==1:
        return 1
    else:
        return n*double_factorial_rec(n-2)
    

#(b)

def increment(lst):
    '''
       Args: lst - list of numbers
       Returns: a list of numbers consisting of each element in lst
       incremented by 1
    '''
    return [i+1 for i in lst] #calls out for using list compression

#(c) See last lab for recursive version. This can be done without
#using a loop at all.

def palindrome(string):
    '''Returns True if string is a palindrome'''

    char_lst = list(string) #Converts to a list of characters
    return char_lst == list(reversed(char_lst)) #List = reverse of list?

#(d)

def remove_all(e,lst):
    '''Remove all occurrences of e from L'''

    return [i for i in lst if i!=e] #again, list compression 



