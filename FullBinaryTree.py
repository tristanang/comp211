##Author: Danny Krizanc
##Date: Nov 2016
##Partial implementation of class FullBinaryTree 


class FullBinaryTree(object):
    '''Implements a full binary tree; each node has exactly two children,
       left and right. For internal nodes left and right are other 
       nodes. For leaves, they are both None. Tree must contain at least
       one node.'''

    def __init__(self,left=None,right=None):

        '''Constructor: left and right are trees;
           default creates tree with a single node'''

        self.left = left
        self.right = right

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





    
