'''Q1'''
def f(fasta):
    fasta = open(fasta,'r')
    genes = fasta.read().split('>')
    lst = []
    for gene in genes[1:]:
        gene_info = gene.split('\n',1)
        lst.append((gene_info[0],gene_info[1].replace('\n','')))
        
    return lst

def test(fasta):
    fasta = open(fasta,'r')
    genes = fasta.read().split('>')
    lst = []
    for gene in genes[1:]:
        gene_info = gene.split('\n',1)
        lst.append((gene_info[0],gene_info[1].rstrip('\n')))
    return lst
    
'''Q2'''
def dist(x,y):
    return (seq_align_score(x,x)+seq_align_score(y,y))/2. - seq_align_score(x,y)

def remove_name(lst):
    '''same the names of the species are useless and that data is thrown away implicitly, why not clean it right now'''
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
    for i in range(len(lst)):
        for j in range(len(lst)):
            assert matrix[i][j] == matrix[j][i]
    return matrix

## score_matrix_v2(remove_name(f('mitochondrial_dna.fasta')))

'''Q3'''
def score_average(matrix):
    ave = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            '''Why waste computational time adding zero and double counting'''
            if i>j:
                ave += 2*matrix[i][j]
    return ave/float(len(matrix)*len(matrix[0]))

## score_average(score_matrix_v2(remove_name(f('mitochondrial_dna.fasta'))))

def test_ave(matrix):
    ave = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            ave += matrix[i][j]
    return ave/float(len(matrix)*len(matrix))

def test(matrix):
    assert test_ave(matrix) == score_average(matrix)
    print 'good stuff'
    
'''Q4'''
def q4script(lst):
    return score_average(score_matrix_v2(rand_dna_lst(remove_name(lst))))
    
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
##def ratio_randomDNA(a,c,g,t):
##    import random
##    dna = ''
##    dna += random.choice("A"*a+"C"*c+"G"*g+"T"*t)
##    return dna

def ratio_rand_dna_lst(lst):
    '''shuffles individual strings in lst'''
    import random
    DNAlst=[''.join(random.sample(str1, len(str1))) for str1 in lst]
    return DNAlst

def testratio(lst):
    lstshuffle=ratio_rand_dna_lst(lst)
    for i in range(len(lst)):
        if countACGT(lst[i]) != countACGT(lstshuffle[i]):
            return 'Failed'
    print 'Passed'

def countACGT(str1):
    '''Count ACGT'''
    a,c,g,t = str1.count('A'),str1.count('C'),str1.count('G'),str1.count('T')
    return a,c,g,t

'''Q6'''

def q6script(lst):
    return score_average(score_matrix_v2(ratio_rand_dna_lst(remove_name(lst))))

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
