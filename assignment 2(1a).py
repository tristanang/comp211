# COMP 211 - Assignment 2
# Tristan Ang & Carlos Eguiluz Rosas  (code slightly different)
# Nov 2016

'''
Problem Functions:
1. alignment(m,n)
2. DPED2(str1,str2,match=1,mismatch=-1,gap=-2)
3. DPED3(str1,str2,match=1,mismatch=-1,gap=-2)
4. score_alignment(align,match=1,mismatch=-1,gap=-2)
'''

################
###QUESTION 1###
################
def alignment(m,n):
    '''create a m by n matrix: Because my primary language is C,
            I prefer making a matrix rather than a dictionary'''
    matrix = [[0 for x in range(n+1)] for y in range(m+1)]
    '''fill up first row and column of matrix with 1'''
    for i in range(m+1):
        matrix[i][0]=1
    for j in range(n+1):
        matrix[0][j]=1
    for i in range(1,m+1):
        for j in range(1,n+1):
            matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j] + matrix[i][j-1]
    return matrix[m][n]

# alignment(20,20) = 260543813797441 for Carlos's computer using same code (both versions)
# alignment(20,20) = 260543813797441L for Tristan's computer using same code (both versions)

################
###QUESTION 2###
################
def DPED2(str1,str2,match=1,mismatch=-1,gap=-2):
    '''Input: two DNA sequences (str) of varying lenghts and int values
               for match, mismatch, and gap
        Output: Returns maximum score as defined by match, mismatch, and gap variables'''
    
    '''Code that will be used again in Q3'''
    matrix = [[0 for x in range(len(str2)+1)] for y in range(len(str1)+1)]
    '''Defining and zeroing a match/mismatch matrix'''
    mm = [[0 for x in range(len(str2))] for y in range(len(str1))]
    
    '''Filling up first row and column'''
    for i in range(len(str1)+1):
        matrix[i][0]=i*gap
    for j in range(1,len(str2)+1):
        matrix[0][j]=j*gap
        
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            '''match/mismatch modifier'''
            if str1[i-1] == str2[j-1]:
                mm[i-1][j-1] = match
            else:
                mm[i-1][j-1] = mismatch
            matrix[i][j]=max(matrix[i-1][j]+gap,matrix[i][j-1]+gap,
                             matrix[i-1][j-1]+mm[i-1][j-1])
    '''Code that will be used again in Q3'''

    '''Returns Maximum Score'''
    return matrix[len(str1)][len(str2)]

################
###QUESTION 3###
################
def DPED3(str1,str2,match=1,mismatch=-1,gap=-2):
    """
        Input: two DNA sequences (str) of varying lenghts and int values
               for match, mismatch, and gap
        Output: Prints the max score (int) for the best/optimal DNA alignment,
                prints that DNA alignment (list), & returns two sequences (str) 
    """

    opalignment=[]

    '''Recycled code begins'''
    matrix = [[0 for x in range(len(str2)+1)] for y in range(len(str1)+1)]
    mm = [[0 for x in range(len(str2))] for y in range(len(str1))]
    for i in range(len(str1)+1):
        matrix[i][0]=i*gap
    for j in range(1,len(str2)+1):
        matrix[0][j]=j*gap
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1] == str2[j-1]:
                mm[i-1][j-1] = match
            else:
                mm[i-1][j-1] = mismatch
            matrix[i][j]=max(matrix[i-1][j]+gap,matrix[i][j-1]+gap,
                             matrix[i-1][j-1]+mm[i-1][j-1])
    '''Recycled code ends'''
    
    '''backwards for loop'''
    i=len(str1)
    j=len(str2)
    '''tracing back the path taken to reach bottom right corner cell'''
    while i>=1 and j>=1:
        if matrix[i][j] - mm[i-1][j-1] == matrix[i-1][j-1]:
            opalignment=[(str1[i-1],str2[j-1])] + opalignment
            i = i-1
            j = j-1
        elif matrix[i][j] - gap == matrix[i][j-1]:
            opalignment=[('-',str2[j-1])] + opalignment
            j = j-1
        elif matrix[i][j] - gap == matrix[i-1][j]:
            opalignment=[(str1[i-1],'-')] + opalignment
            i = i-1
        else:
            print 'error'

    '''Inputs empty spaces'''
    while i>=1:
        opalignment=[(str1[i-1],'-')]+opalignment
        i = i-1
    while j>=1:
        opalignment=[('-',str2[j-1])]+opalignment
        j = j-1
                
    print 'Score = '+str(matrix[len(str1)][len(str2)])+''
    print printer_helper((opalignment))
    return opalignment

def printer_helper(opt_align): 
    """
        Input: an alignment (opt_align) stored as a list of pairs
        Output: prints the two sequences (str)        
    """
    # prints each sequence seperately
    align1,align2 = "",""
    for (i,j) in opt_align: 
        align1 += i   
        align2 += j   
    return align1+"\n"+align2

################
###QUESTION 4###
################

def score_alignment(align,match=1,mismatch=-1,gap=-2):
    score = 0
    """
        input: a DNA sequence alignment (list). User has the option
               to find values for match, mismatch and gap 
        output: the max alignment score (int)
    """
    for (i,j) in align:
        if i==j:
            score += match
        elif i=="-" or j=="-":
            score += gap
        else:
            score += mismatch
    return score

####################
###TEST FUNCTIONS###
####################

'''Q1'''
def alignmenttest(n):
    """
        input: a positive integer n
        output: prints "It's lit." if function alignment passes test.
                prints "Oh no!" otherwise.
        *the inverse of (i,j) is equal to (i,j)
    """
    for i in range(n+1):
        for j in range(n+1):
            if alignment(i,j) != alignment(j,i):
                print 'Oh no!'
    print "It's lit."

'''Q2'''
def randomDNA(n):
    import random
    dna = ''
    for i in range(n):
        dna = dna +random.choice('ACGT')
    return dna

def test_ED(f=DPED2,match=1,mismatch=-1,gap=-2):
    ''' Tests DPED2'''   
    assert f('','',match,mismatch,gap) == 0
    assert f('','aaaaa',match,mismatch,gap) == 5*gap
    assert f('aaaaa','',match,mismatch,gap) == 5*gap
    assert f('aaaaa','bbbbb',match,mismatch,gap) == max(5*gap,5*mismatch)
    assert f('aaaaa','aaaaa',match,mismatch,gap) == 5*match
    assert f('aaaaa','aabaa',match,mismatch,gap) == 4*match+max(gap,mismatch)
    assert f('aaaa','aabaa',match,mismatch,gap) == 4*match+gap
    assert f('aabaa','aaaa',match,mismatch,gap) == 4*match+gap
    assert f('abcdefg','bcdefga',match,mismatch,gap) == max(7*mismatch,6*match+2*gap)
    DNA = randomDNA(10)
    assert f(DNA,DNA[::-1]) == f(DNA[::-1],DNA)
    DNA1 = randomDNA(500)
    DNA2 = randomDNA(500)
    assert f(DNA1,DNA2) == f(DNA2,DNA1)
    print "passed all tests"

def test_ED_rand(a,b,f=DPED2):
    '''
       Tests Problem #2 with random module
       Input: two int values a,b where a<=b
    '''
    if a>b:
        a,b = b,a
    import random

    match = random.randint(a, b)
    mismatch = match - abs(random.randint(a, b))
    gap = mismatch - abs(random.randint(a, b))
   
    assert f('','',match,mismatch,gap) == 0
    assert f('','aaaaa',match,mismatch,gap) == 5*gap
    assert f('aaaaa','',match,mismatch,gap) == 5*gap
    assert f('aaaaa','bbbbb',match,mismatch,gap) == max(5*gap,5*mismatch)
    assert f('aaaaa','aaaaa',match,mismatch,gap) == 5*match
    assert f('aaaaa','aabaa',match,mismatch,gap) == 4*match+max(gap,mismatch)
    assert f('aaaa','aabaa',match,mismatch,gap) == 4*match+gap
    assert f('aabaa','aaaa',match,mismatch,gap) == 4*match+gap
    assert f('abcdefg','bcdefga',match,mismatch,gap) == max(7*mismatch,6*match+2*gap)
    DNA = randomDNA(10)
    assert f(DNA,DNA[::-1]) == f(DNA[::-1],DNA)
    DNA1 = randomDNA(500)
    DNA2 = randomDNA(500)
    assert f(DNA1,DNA2) == f(DNA2,DNA1)
    print "passed all tests"



def test_alignment(f=DPED3,a=score_alignment,g=DPED2):
    """
        Tests problems 3 & 4 mainly, but uses 2.
    """
    import random

    match = random.randint(0, 500)
    mismatch = match - abs(random.randint(0, 500))
    gap = mismatch - abs(random.randint(0, 500))

    DNA1 = randomDNA(500)
    DNA2 = randomDNA(500)

    assert g(DNA1,DNA2,match,mismatch,gap) == a(f(DNA1,DNA2,match,mismatch,gap),match,mismatch,gap)
    print 'winner winner chicken dinner'
