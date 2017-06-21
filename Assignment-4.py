# COOL NAME
# Nov 2016

################
###QUESTION 1###
################

class FullBinaryTree(object):
    '''Implements a full binary tree; each node has exactly two children,
       left and right. For internal nodes left and right are other 
       nodes. For leaves, they are both None. Tree must contain at least
       one node.'''

    def __init__(self,left=None,right=None,parent=None):

        '''
           Constructor: left and right are trees;
           default creates tree with a single node
        '''

        self.left = left
        self.right = right
        self.parent = None
        if left != None:
            left.parent = self
        if right != None:
            right.parent = self

    def is_leaf(self):

        '''Returns True if Tree is a leaf'''

        return not self.left and not self.right

    def size(self):
        '''Returns the size (number of nodes) of tree'''
        if self.is_leaf():
            return 1
        else:
            return 1 + self.left.size() + self.right.size()

    def height(self):
        '''Returns the height (longest root to leaf path) of tree'''
        if self.is_leaf():
            return 0
        else:
            return 1 + max((self.left.height(),self.right.height()))

    def is_root(self):
        '''Returns True if is root, False is not'''
        return self.parent == None

    def find_root(self):
        '''Recursive search for finding root; going searching by leaf along
           stem'''        
        if self.is_root():
            return self
        else:
            find_root(self.parent)

    def list_of_leaves(self):
        lst = []
        if self.is_leaf():
            lst.append(self)
            return lst
        else:
            return self.left.list_of_leaves() + self.right.list_of_leaves()

##a = FullBinaryTree()
##b = FullBinaryTree()
##c = FullBinaryTree(a,b)
##d = FullBinaryTree()
##e = FullBinaryTree()
##f = FullBinaryTree(d,e)
##g = FullBinaryTree(c,f)
##h = FullBinaryTree()
##i = FullBinaryTree(g,h)

def testFBT2():
    a = FullBinaryTree()
    b = FullBinaryTree()
    c = FullBinaryTree(a,b)
    d = FullBinaryTree()
    e = FullBinaryTree()
    f = FullBinaryTree(d,e)
    g = FullBinaryTree(c,f)
    h = FullBinaryTree()
    i = FullBinaryTree(g,h)
    assert a.parent == c
    assert b.parent == c
    assert d.parent == e.parent == f
    assert c.parent == f.parent == g
    assert g.parent == h.parent == i
    assert i.is_root()
    for j in (a,b,c,d,e,f,g,h):
        assert not j.is_root()
    print "passed all tests"

def testFBT():
    '''Very small test of FBT'''

    a = FullBinaryTree()
    b = FullBinaryTree()
    c = FullBinaryTree(a,b)
    d = FullBinaryTree()
    e = FullBinaryTree()
    f = FullBinaryTree(d,e)
    g = FullBinaryTree(c,f)
    h = FullBinaryTree()
    i = FullBinaryTree(g,h)
    assert a.size() == 1
    assert a.is_leaf()
    assert a.height() == 0
    assert not i.is_leaf()
    assert i.size() == 9
    assert i.height() == 3
    print "passed all tests"

'''Q2'''
class PhyloTree(FullBinaryTree):
    
    def __init__(self,name,left=None,right=None,parent=None,time=0.0):
        self.name = name
        self.time = time
        FullBinaryTree.__init__(self,left,right,parent)

    def __eq__(self,other):
        return repr(self) == repr(other)
    
    def __str__(self):
        if self.is_leaf():
            return str(self.name)
        else:
            return '('+str(self.left)+','+str(self.right)+')'

    def get_time(self):
        return self.time

    def get_species(self,name):
        if self.is_leaf() and self.name == name:
            return self
        elif self.is_leaf() or self.name == name:
            return None
        else:
            return self.left.get_species(name) or self.right.get_species(name)

    def lca(self,other):
        selfancestors=[self]
        otherancestors=[other]
        selfparent=self.parent
        otherparent=other.parent
        while selfparent != None:
            selfancestors.append(selfparent)
            selfparent = selfparent.parent
        while otherparent != None:
            otherancestors.append(otherparent)
            otherparent = otherparent.parent
        for i in selfancestors:
            if i in otherancestors:
                return i
        return None
##def testPhylostring():
##    a = PhyloTree()
##    b = PhyloTree()
##    c = PhyloTree(a,b)
##    d = PhyloTree()
##    e = PhyloTree()
##    f = PhyloTree(d,e)
##    g = PhyloTree(c,f)
##    h = PhyloTree()
##    i = PhyloTree(g,h)

a = PhyloTree('Dog')
b = PhyloTree('Cat')
c = PhyloTree('CatDog',a,b)
d = PhyloTree('Cow')
e = PhyloTree('Chicken')
f = PhyloTree('CowChicken',d,e)
g = PhyloTree('OP',c,f)
h = PhyloTree('pem')
i = PhyloTree('man',g,h)

def UPGMAa2(names,matrix):
    '''
        Input: a list of species names (names) & a matrix of their distances
        Output: Returns a PhyloTree object containing the root of the resulting
                UPGMA tree
    '''
    import copy
    memo={}
    init_leaf(names,memo)
    umatrix = copy.deepcopy(list(matrix)) ##Creates a copy of matrix containing distances
    cluster = [[i] for i in range(len(matrix))] ##initialize size one clusters
    unames = list(names) ##could be fused with cluster but i felt it was cleaner this way
    
    while len(cluster) > 1:
        x,y = closest_pair(umatrix)
        '''add new ancestor'''
        
        memo[unames[x]+unames[y]] = PhyloTree(unames[x]+unames[y], memo[unames[x]], memo[unames[y]], None, umatrix[x][y]/2)
        root = memo[unames[x]+unames[y]] ##current root
        
        for j in range(len(umatrix)): ##zero out row
            umatrix[x][j]=0
            
        cluster[x] = cluster[x]+cluster[y] ##forming cluster in 2 step process
        cluster = cluster[0:y]+cluster[y+1::] ##forming cluster in 2 step process
        
        unames[x] += unames[y] ##corresponding names cluster
        unames = unames[0:y]+unames[y+1::] 
        
        umatrix = remove_column(y,umatrix)
        umatrix = umatrix[0:y]+umatrix[y+1::] ##removes row y from matrix
        
        for i in range(len(cluster)):
            if i!=x:
                pairs=pair_generator(cluster[x],cluster[i])
                for pair in pairs:
                    p,q=pair ##p,q references the original matrix indices
                    umatrix[x][i] += matrix[p][q]/(len(pairs)) ##[x][i references updated matrix index
                    ##all p,q belongs to umatrix[x][i]
                    
        for j in range(len(umatrix)): ##matrix reflection for pivotal row
            umatrix[j][x]=umatrix[x][j] ##right hand side is the updated values

    return root

    
def remove_column(column,matrix):
    '''Returns a matrix with nth column removed; ('column' = int)'''
    for i in range(len(matrix)):
        matrix[i] = matrix[i][0:column] + matrix[i][column+1::]
    return matrix

def pair_generator(a,b):
    '''Returns a list with all the possible leaf cominations in a tree'''
    return [(x,y) for x in a for y in b]
        
def closest_pair(matrix):
    '''Returns a pair of coordinates within a matrix'''
    minimum=float("inf")#In order for loop to initiate and then work after condit. holds  
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if minimum > matrix[i][j] and j>i:#the first part of condition holds w/ 'inf' j>i because we only need consider one triangle or matrix
                minimum = matrix[i][j]
                indexi = i
                indexj = j
    return indexi,indexj

def init_leaf(names,memo):
     '''initializes all leafs into memo'''
    for name in names:
        memo[name]=PhyloTree(name)


'''Same result achieved. This should not be a surprising result. How you calculated it?'''
 
'''Appendix'''
matrix = [[0.0, 1598.5, 1424.0, 1411.0, 1559.5, 1049.0, 947.0, 906.0, 825.0, 1401.0], [1598.5, 0.0, 1544.5, 1709.5, 1008.0, 1523.5, 1538.5, 1548.5, 1482.5, 1230.5], [1424.0, 1544.5, 0.0, 1494.0, 1624.5, 1431.0, 1393.0, 1454.0, 1414.0, 1367.0], [1411.0, 1709.5, 1494.0, 0.0, 1687.5, 1364.0, 1343.0, 1446.0, 1290.0, 1564.0], [1559.5, 1008.0, 1624.5, 1687.5, 0.0, 1590.5, 1500.5, 1580.5, 1545.5, 1303.5], [1049.0, 1523.5, 1431.0, 1364.0, 1590.5, 0.0, 714.0, 1022.0, 1039.0, 1341.0], [947.0, 1538.5, 1393.0, 1343.0, 1500.5, 714.0, 0.0, 1066.0, 1010.0, 1389.0], [906.0, 1548.5, 1454.0, 1446.0, 1580.5, 1022.0, 1066.0, 0.0, 924.0, 1453.0], [825.0, 1482.5, 1414.0, 1290.0, 1545.5, 1039.0, 1010.0, 924.0, 0.0, 1337.0], [1401.0, 1230.5, 1367.0, 1564.0, 1303.5, 1341.0, 1389.0, 1453.0, 1337.0, 0.0]]
names = ['Cow','Carp','Chicken','Human','Loach','Mouse','Rat','Seal','Whale','Frog']

testmatrix = [[0.0, 19.0, 27.0, 8.0, 33.0, 18.0, 13.0], [19.0, 0.0, 31.0, 18.0, 36.0, 1.0, 13.0], [27.0, 31.0, 0.0, 26.0, 41.0, 32.0, 29.0], [8.0, 18.0, 26.0, 0.0, 31.0, 17.0, 14.0], [33.0, 36.0, 41.0, 31.0, 0.0, 35.0, 28.0],
          [18.0, 1.0, 32.0, 17.0, 35.0, 0.0, 12.0], [13.0, 13.0, 29.0, 14.0, 28.0, 12.0, 0.0]]

testmatrix2=[[0, 18.0, 26.5, 32.0, 13.5], [18.0, 0, 31.5, 35.5, 12.5], [26.5, 31.5, 0, 41.0, 29.0], [32.0, 35.5, 41.0, 0, 28.0], [13.5, 12.5, 29.0, 28.0, 0]]
testnames=['A','B','C','D','E','F','G']
root = UPGMAa2(names,matrix)
