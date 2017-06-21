# Tristan Ang Tze Heng & Carlos Rosas
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

        '''Returns True if node is a leaf'''

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

    def num_leaves(self):
        if self.is_leaf():
            return 1
        else:
            return self.left.num_leaves() + self.right.num_leaves()

    
    def list_of_leaves(self):
        if self.is_leaf():
            return [self]
        else:
            return self.left.list_of_leaves() + self.right.list_of_leaves()

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

################
###QUESTION 2###
################
    
class PhyloTree(FullBinaryTree):
    
    def __init__(self,symbol,prob,code,left=None,right=None,parent=None):
        self.symbol = symbol
        self.prob = prob
        self.code = code
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

def testPT():
    a = PhyloTree('Dog')
    b = PhyloTree('Cat')
    c = PhyloTree('CatDog',a,b)
    d = PhyloTree('Cow')
    e = PhyloTree('Chicken')
    f = PhyloTree('CowChicken',d,e)
    g = PhyloTree('OP',c,f)
    h = PhyloTree('pem')
    i = PhyloTree('man',g,h)
    print i.num_leaves()
    assert a.is_leaf()
    assert b.is_leaf()
    assert d.is_leaf()
    assert e.is_leaf()
    assert h.is_leaf()
    assert a.lca(b) == b.lca(a) == c
    assert d.lca(e) == e.lca(d) == f
    leaves = i.list_of_leaves()
    print 'yea passed'

################
###QUESTION 3###
################
    
def UPGMAa2(names,matrix): ##a2 because first attempt was bad
    memo={}
    init_leaf(names,memo)
    import copy
    umatrix = copy.deepcopy(list(matrix))
    unames = list(names) ##could be fused with cluster but i felt it was cleaner this way
    cluster=[] ##unames and cluster record the clusters
    for i in range(len(matrix)): ##initialize size one clusters
        cluster.append([i])
    while len(cluster) > 1:
        x,y = closest_pair(umatrix)
        '''add new ancestor'''
        memo[unames[x]+unames[y]]=PhyloTree(unames[x]+unames[y],memo[unames[x]],memo[unames[y]],None,umatrix[x][y]/2)
        root = memo[unames[x]+unames[y]] ##current root
        for j in range(len(umatrix)): ##zero out row
            umatrix[x][j]=0
        cluster[x] = cluster[x]+cluster[y] ##updating cluster in 2 step process
        cluster = cluster[0:y]+cluster[y+1::] ##updating cluster in 2 step process
        unames[x] += unames[y] ##corresponding upate of names cluster
        unames = unames[0:y]+unames[y+1::] 
        umatrix = remove_column(y,umatrix)
        umatrix = umatrix[0:y]+umatrix[y+1::] ##removes row y from matrix
        for i in range(len(cluster)):
            if i!=x:
                pairs=pair_generator(cluster[x],cluster[i])
                for pair in pairs:
                    p,q=pair ##p,q references the original matrix indices
                    umatrix[x][i] += matrix[p][q]/(len(pairs)) ##[x][i] references updated matrix index
                    ##all p,q belongs to umatrix[x][i]      
        for j in range(len(umatrix)): ##matrix reflection for updated row, updates respective column
            umatrix[j][x]=umatrix[x][j] ##right hand side is the updated values
##        for i in range(len(umatrix)):
##            assert umatrix[i][i]==0
    return root

    
def remove_column(column,matrix):
    for i in range(len(matrix)):
        matrix[i]=matrix[i][0:column]+matrix[i][column+1::]
    return matrix

def pair_generator(a,b):
    return [(x,y) for x in a for y in b]
        
def closest_pair(matrix):
    minimum=float("inf")
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if minimum > matrix[i][j] and j>i:
                minimum = matrix[i][j]
                indexi = i
                indexj = j
    return indexi,indexj

def init_leaf(names,memo):
    '''initializes all leafs into memo'''
    for name in names:
        memo[name]=PhyloTree(name)

################
###QUESTION 4###
################
        
def main(names,matrix):
    root = UPGMAa2(names,matrix) 
    print str(root) ##((((((Cow,Whale),Seal),(Mouse,Rat)),Human),Chicken),((Carp,Loach),Frog))
    human = root.get_species('Human')
    cow = root.get_species('Cow')
    human_cow_lca = human.lca(cow)
    print str(human_cow_lca) ##((((Cow,Whale),Seal),(Mouse,Rat)),Human)
    print human_cow_lca.time ##685.4
    
################
###QUESTION 5###
################
    
def tree_to_matrix(root):
    leaves= root.list_of_leaves()
    matrix = [[0 for x in range(len(leaves))] for y in range(len(leaves))]
    average=0.0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i>j:
                matrix[i][j]=matrix[j][i]=distance(leaves[i],leaves[j])
                average += (2*matrix[i][j])/(len(matrix)*len(matrix)-len(matrix))
    #print matrix
    return average ## 1342.088888

def distance(species1,species2):
    if species1 == species2:
        return 0.0
    lca=species1.lca(species2)
    return lca.time*2.

'''Same result achieved. This should not be a surprising result. How you calculated it?'''
 
'''Appendix'''
matrix = [[0.0, 1598.5, 1424.0, 1411.0, 1559.5, 1049.0, 947.0, 906.0, 825.0, 1401.0], [1598.5, 0.0, 1544.5, 1709.5, 1008.0, 1523.5, 1538.5, 1548.5, 1482.5, 1230.5], [1424.0, 1544.5, 0.0, 1494.0, 1624.5, 1431.0, 1393.0, 1454.0, 1414.0, 1367.0], [1411.0, 1709.5, 1494.0, 0.0, 1687.5, 1364.0, 1343.0, 1446.0, 1290.0, 1564.0], [1559.5, 1008.0, 1624.5, 1687.5, 0.0, 1590.5, 1500.5, 1580.5, 1545.5, 1303.5], [1049.0, 1523.5, 1431.0, 1364.0, 1590.5, 0.0, 714.0, 1022.0, 1039.0, 1341.0], [947.0, 1538.5, 1393.0, 1343.0, 1500.5, 714.0, 0.0, 1066.0, 1010.0, 1389.0], [906.0, 1548.5, 1454.0, 1446.0, 1580.5, 1022.0, 1066.0, 0.0, 924.0, 1453.0], [825.0, 1482.5, 1414.0, 1290.0, 1545.5, 1039.0, 1010.0, 924.0, 0.0, 1337.0], [1401.0, 1230.5, 1367.0, 1564.0, 1303.5, 1341.0, 1389.0, 1453.0, 1337.0, 0.0]]
names = ['Cow','Carp','Chicken','Human','Loach','Mouse','Rat','Seal','Whale','Frog']

testmatrix = [[0.0, 19.0, 27.0, 8.0, 33.0, 18.0, 13.0], [19.0, 0.0, 31.0, 18.0, 36.0, 1.0, 13.0], [27.0, 31.0, 0.0, 26.0, 41.0, 32.0, 29.0], [8.0, 18.0, 26.0, 0.0, 31.0, 17.0, 14.0], [33.0, 36.0, 41.0, 31.0, 0.0, 35.0, 28.0],
          [18.0, 1.0, 32.0, 17.0, 35.0, 0.0, 12.0], [13.0, 13.0, 29.0, 14.0, 28.0, 12.0, 0.0]]

testmatrix2=[[0, 18.0, 26.5, 32.0, 13.5], [18.0, 0, 31.5, 35.5, 12.5], [26.5, 31.5, 0, 41.0, 29.0], [32.0, 35.5, 41.0, 0, 28.0], [13.5, 12.5, 29.0, 28.0, 0]]
testnames=['A','B','C','D','E','F','G']
root = UPGMAa2(names,matrix)
