'''Q1'''
def f(fasta):
    lst = []
    fasta = open(fasta,'r')
    genes = fasta.read().split('>') #Reads all of file at once! (lab docstring)
    for gene in genes[1:]: #Note: before first '>' is an empty gene
        gene_info = gene.split('\n',1)  # split off first line of gene
        lst.append((gene_info[0],gene_info[1].replace('\n',''))) #appends tuple to list. replace module removes all '\n'
    return lst

def test(fasta):
    '''test function I used to make sure I remove '\n' properly,
        input file is mitochondrial_dna.fasta with manual editing such that gene appears in single line.'''
    fasta = open(fasta,'r')
    genes = fasta.read().split('>')
    lst = []
    for gene in genes[1:]:
        gene_info = gene.split('\n',1)
        lst.append((gene_info[0],gene_info[1].rstrip('\n')))
    return lst
    
'''Q2'''
def dist(x,y):
    return (len(x)*MATCH+len(y)*MATCH)/2. - seq_align_score(x,y) #using formula given

def remove_name(lst):
    '''removes the names of the species, such that score_matrix_v2 works for later parts without editing'''
    clean=[]
    for i in range(len(lst)):
        clean += [lst[i][1]]
    return clean
        
def score_matrix_v2(lst):
    matrix = [[0 for x in range(len(lst))] for y in range(len(lst))]
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i==j:
                matrix[i][j]=0
            elif i>j:
                matrix[i][j]=matrix[j][i]
            else:
                matrix[i][j] = dist(lst[i],lst[j])
##    for i in range(len(lst)): 
##        for j in range(len(lst)):
##            assert matrix[i][j] == matrix[j][i] #checks condition for entire matrix
    return matrix

def q2script(lst):
    lst1 = remove_name(lst)
    return score_matrix_v2(lst1)

## q2script(f('mitochondrial_dna.fasta'))

'''Q3'''
def score_average(matrix):
    ave = 0
    for i in range(len(matrix)): #calculates the average for the upper right triangle of matrix
        for j in range(len(matrix)):
            if j>i:
                ave += matrix[i][j]
                ##print matrix[i][j]
    return ave/(0.5*(len(matrix)*len(matrix)-len(matrix)))

def q3script(tuplelst):
    lst = remove_name(tuplelst)
    matrix = score_matrix_v2(lst)
    return score_average(matrix)

## q3script(f('mitochondrial_dna.fasta'))

'''Q4'''
def q4script(lst):
    lst = remove_name(lst)
    lst1 = rand_dna_lst(lst)
    matrix = score_matrix_v2(lst1)
    return score_average(matrix)

def rand_dna_lst(lst):
    '''takes input real list and generates random list with similar dna lengths'''
    DNAlst=[]
    for i in range(len(lst)):
        DNAlst.append(randomDNA(len(lst[i])))
    return DNAlst

def randomDNA(n):
    '''Generates random DNA sequence of length n'''
    import random
    dna = ''
    for i in range(n):
        dna = dna +random.choice('ACGT')
    return dna

## q4script(f('mitochondrial_dna.fasta'))
            
'''Q5'''
## dictionary
##def ratio_randomDNA(a,c,g,t):
##    import random
##    dna = ''
##    dna += random.choice("A"*a+"C"*c+"G"*g+"T"*t)
##    return dna

def q5script(lst):
    lst = remove_name(lst)
    return ratio_rand_dna_lst(lst)

def ratio_rand_dna_lst(lst):
    '''shuffles individual strings in lst'''
    import random
    '''needs excellent doc string'''
    DNAlst=[''.join(random.sample(str1, len(str1))) for str1 in lst] #using random.sample to select elements without replacement
    return DNAlst

def testratio(lst):
    '''check if shuffle function above works'''
    lstshuffle=ratio_rand_dna_lst(lst)
    for i in range(len(lst)):
        if countACGT(lst[i]) != countACGT(lstshuffle[i]): 
            return 'Failed' #If shuffle works then the count of A,T,C,G should be equal
    print 'Passed'

def countACGT(str1):
    '''Count ACGT'''
    a,c,g,t = str1.count('A'),str1.count('C'),str1.count('G'),str1.count('T')
    return a,c,g,t

# q5script(f('mitochondrial_dna.fasta'))

'''Q6'''
def q6script(lst):
    lst1 = q5script(lst)
    matrix = score_matrix_v2(lst1)
    return score_average(matrix)
    
'''Q7'''
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
    
'''Appendix'''
MATCH = 5
MISMATCH = -2
GAP = -6            

def seq_align_scoring_matrix(str1,str2):
    
    '''Returns the dynamic programming scoring matrix for the global
       alignment of str1 and str2 assuming the constant costs associated
       with MATCH, MISMATCH, and GAP are defined as global variables.'''

    memo = {}
    memo[(0,0)] = 0
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
