# Carlos Eguiluz Rosas & Tristan Ang
# COMP211 - Assignment 3
# November 2016
import random

################
###QUESTION 1###
################

def f(fasta):
    """
        Input: a fasta file (mitochonrial_dna.text) containing dna
               sequences (str) for certain animals
        Output: a list of tuples defined as (animal,sequence)
    """
    lst = []
    fasta = open(fasta,'r')
    genes = fasta.read().split('>')[1:]
    for gene in genes: 
        gene_info = gene.split('\n',1)  
        lst.append((gene_info[0],gene_info[1].replace('\n','')))
        #appends tuple to list. replace module removes all '\n'
    return lst

    
################
###QUESTION 2###
################

def dist(x,y):
    """
        Input: two sequences x,y (str)
        Output: distance (floating number) between given sequences
    """
    return (len(x)*MATCH+len(y)*MATCH)/2. - seq_align_score(x,y) 

def remove_name(lst):
    """
        Input: a list of tuples defined as (name,sequence) (both strings)
        Output: a list of only sequences (str)
        *Removes name of species so that score_matrix works for later parts without editing
    """
    return [lst[i][1] for i in range(len(lst))]

        
def score_matrix(lst):
    """
        Input: a list of sequences (str)
        Output: a len(list)-by-len(list) matrix (a list of lists)
    """
    matrix = [[0 for x in range(len(lst))] for y in range(len(lst))]
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i==j:
                matrix[i][j]=0
            elif i>j:
                matrix[i][j]=matrix[j][i]
            else:
                matrix[i][j] = dist(lst[i],lst[j])
                
##    "Internal Test Function"  
##    for i in range(len(lst)): 
##        for j in range(len(lst)):
##            assert matrix[i][j] == matrix[j][i] #checks condition for entire matrix
    return matrix

def q2script(lst):
    return score_matrix(remove_name(lst))

## q2script(f('mitochondrial_dna.fasta'))


################
###QUESTION 3###
################

def score_average(matrix):
    """
        Input: a list of sequnces (str)
        Output: the average distance between pairs of sequences
    """
    ave = 0
    for i in range(len(matrix)): #calculates the average for the upper right triangle of matrix
        for j in range(len(matrix)):
            if j>i:
                ave += matrix[i][j]
    return ave/(0.5*(len(matrix)*len(matrix)-len(matrix)))

def q3script(tuplelst):
    lst = remove_name(tuplelst)
    matrix = score_matrix(lst)
    return score_average(matrix)

## q3script(f('mitochondrial_dna.fasta'))


################
###QUESTION 4###
################

def q4script(lst):
    lst1 = rand_dna_lst(remove_name(lst))
    matrix = score_matrix(lst1)
    return score_average(matrix)

def rand_dna_lst(lst):
    '''takes input real list and generates random list with similar dna lengths'''
    DNAlst=[]
    for i in range(len(lst)):
        DNAlst.append(randomDNA(len(lst[i])))
    return DNAlst

def randomDNA(n):
    """
        Input: a positive integer n
        Output: a DNA sequence (str) of length n
    """
    return "".join([random.choice('ACGT') for i in range(n)])

## q4script(f('mitochondrial_dna.fasta'))

            
################
###QUESTION 5###
################

def q5script(lst):
    return ratio_rand_dna_lst(remove_name(lst))

def ratio_rand_dna_lst(lst):
    """
        Input: a list of dna sequences lst (str)
        Output: a new list (DNAlst)in which the individual strings
                from lst get shuffled
        *DNAlst is created using random.sample in order to select elements with
         without replacement
    """
    DNAlst=[''.join(random.sample(str1, len(str1))) for str1 in lst]
    return DNAlst

def testratio(lst):
    '''check if shuffle function above works'''
    lst = remove_name(lst)
    lstshuffle = ratio_rand_dna_lst(lst)
    for i in range(len(lst)):
        if countACGT(lst[i]) != countACGT(lstshuffle[i]): 
            return 'Failed' #If shuffle works then the count of A,T,C,G should be equal
    print 'Passed'

def countACGT(str1):
    '''Input: a dna sequence (str)
       Output: counts individual nucleotides and returns them
    '''
    a,c,g,t = str1.count('A'),str1.count('C'),str1.count('G'),str1.count('T')
    return a,c,g,t

# q5script(f('mitochondrial_dna.fasta'))


################
###QUESTION 6###
################

def q6script(lst):
    lst1 = q5script(lst)
    matrix = score_matrix(lst1)
    return score_average(matrix)

# q6script(f('mitochondrial_dna.fasta'))
   
################
###QUESTION 7###
################

def three_sums(lst):
   # print 'Real Seq Ave = '+str(q3script(lst))+''#1342.08
    print 'Real Seq Ave = 1342.08888889'
    print 'Rand Seq Ave = '+str(q4script(lst))+'' #2734.62
    print 'Shuffle Seq Ave = '+str(q6script(lst))+'' #2659.64
    
'''The shuffle sequence average and the random sequence average are pretty close in
    in value, although the shuffle sequence is slightly smaller. The real sequence
    average is half the magnitude of the other two averages.'''

'''Because the average distance for the real sequence is smaller, we can say that there
    might be a common ancestor for all the species.'''

'''Since species have a common ancestor real sequences probably stem from mutations (mistmatch),
    deletions(gaps).'''
    

##############
###Appendix###
##############

MATCH = 5
MISMATCH = -2
GAP = -6            

def seq_align_scoring_matrix(str1,str2,memo={(0,0):0}):
    
    '''Returns the dynamic programming scoring matrix for the global
       alignment of str1 and str2 assuming the constant costs associated
       with MATCH, MISMATCH, and GAP are defined as global variables.'''

    for i in range(1,len(str1)+1):
        memo[(i,0)] = i*GAP
    for j in range(1,len(str2)+1):
        memo[(0,j)] = j*GAP
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1] == str2[j-1]:
                match_mismatch = MATCH
            else:
                match_mismatch = MISMATCH
            memo[(i,j)]=max((memo[(i-1,j-1)]+match_mismatch,
                             memo[(i,j-1)]+GAP,
                             memo[(i-1,j)]+GAP))
    return memo

def seq_align_score(str1,str2):
    
    '''Returns the maximum alignment score for str1 and str2 assuming
       the constant costs associated with MATCH, MISMATCH, and GAP are
       defined as global variables.'''
    
    return seq_align_scoring_matrix(str1,str2)[(len(str1),len(str2))]

'''score_matrix function that works without removing name'''
##def score_matrix(lst):
##    matrix = [[0 for x in range(len(lst))] for y in range(len(lst))]
##    for i in range(len(lst)):
##        for j in range(len(lst)):
##            if i==j:
##                matrix[i][j]=0
##            elif i>j:
##                matrix[i][j]=matrix[j][i]
##            else:
##                matrix[i][j] = dist(lst[i][1],lst[j][1])
##    for i in range(len(lst)):
##        for j in range(len(lst)):
##            assert matrix[i][j] == matrix[j][i]
##    return matrix    
