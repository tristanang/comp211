class FullBinaryTree(object):

    '''Implements a full binary tree; each node should have exactly two children,
       left and right, and one parent. For interal nodes left and right are
       are other internal nodes. For leaves, the are both None. All nodes
       have a parent that is an internal node except the root whose parent
       is None. Tree must contain at least one node.'''

    def __init__(self,left=None,right=None,parent=None):

        '''Constructor creates a single node tree as default. Sets
           parent relation if left and right are given.'''

        self.left = left
        self.right = right
        self.parent = parent
        if self.left:
            self.left.set_parent(self)
        if self.right:
            self.right.set_parent(self)

    def set_parent(self,tree):

        self.parent = tree

    def get_parent(self):

        return self.parent

    def is_leaf(self):

        '''Returns true iff node is a leaf'''

        return not self.left and not self.right

    def is_root(self):

        '''Returns true iff node is the root'''

        return not self.parent

    def contains(self,tree):

        '''Returns true iff self contains tree as a subtree'''

        if self == tree:
            return True
        elif self.is_leaf():
            return False
        else:
            return self.left.contains(tree) or self.right.contains(tree)

    def list_of_leaves(self):

        '''Returns a list of all of the leaves of tree'''

        if self.is_leaf():
            return [self]
        else:
            return self.left.list_of_leaves()+self.right.list_of_leaves()

        
class HuffmanTree(FullBinaryTree):
    def __init__(self,symbol,prob=0,left=None,right=None,code=None,parent=None):
        self.symbol = symbol
        self.prob = prob
        self.code = code
        FullBinaryTree.__init__(self,left,right,parent=None)
        self.set_prob()
        if left and right:
            self.set_code()

    def set_prob(self):
        if not self.is_leaf():
            self.prob = self.left.prob + self.right.prob

    def set_code(self):
        self.left.code='0'
        self.right.code='1'


    def __cmp__(self,other):
        return cmp(self.prob, other.prob)

    def get_root(self):
        if self.parent == None:
            return self
        else:
            return self.parent.get_root()

    def get_symbol(self, symbol):

        leaves = self.list_of_leaves()
        for leaf in leaves:
            if leaf.symbol == symbol:
                return leaf
        return None

##    def get_codeword(self):
##        if self.is_root():
##            return ''
##        return self.parent.get_codeword() + str(self.code)
##    
##
    def get_codeword(self):
        if self.is_root():
            return ''
        else:
            return self.parent.get_codeword() + self.code

    def get_symbol(self,symbol):
        leaves = self.list_of_leaves()
        for leaf in leaves:
            if leaf.symbol == symbol:
                return leaf
        return None

    def get_symbol(self,symbol):
        if self.is_leaf():
            if self == symbol:
                return True
            else:
                return None
        else:
            self.left.contains(symbol) or self.right.contains(symbol)

##3
import io
import math
import random
import collections
def file_get_string(n, string, newFile):
    randomStr = []
    i = 1
    open(newFile, 'w+')
    while i <= len(n):
        randomStr.append(random.choice(n))
        i += 1
    newFile = open(newFile, 'a+')
    newFile.write(''.join(randomStr))

##def str_of_file(File):
##    with open(File, 'r') as myfile:
##        #data=myfile.read().replace('\n', '')
##        data=myfile.read()
##    return data

def compare_strings(File1, File2):
    x = str_of_file(File1)
    y = str_of_file(File2)
    if x ==y:
        return True
    else:
        return False

def calculate_probability(n):
    dictionary = collections.Counter(n)
    newDict = {}
    for x in n:
        newDict[x] = dictionary[x]/float(len(n))
    return newDict

def entropy(n):
    dictionary = calculate_probability(n)
    entropy = 0
    for x in dictionary:
        entropy = entropy + float(dictionary[x]) * float(math.log((1/dictionary[x]),2))
    return entropy

    
            

##2
import heapq
def HuffTree(newDict):
    LL1 = []
    for x in newDict:
        y = (newDict[x],HuffmanTree(x, newDict[x], code=None, left=None, right=None, parent=None))
        LL1.append(y)
    heapq.heapify(LL1)
    while len(LL1) > 1:
        y = heapq.heappop(LL1)
        x = heapq.heappop(LL1)
        newTree = (x[0]+y[0],HuffmanTree(symbol=y[1].symbol+x[1].symbol,left=y[1],right=x[1]))
        heapq.heappush(LL1, newTree)
    return LL1[0][1]

def dcode(newDict):
    Tree = HuffTree(newDict)
    variable = Tree.list_of_leaves()
    code_dict = {}
    for x in variable:
        codee = x.symbol
        code_dict[codee] = x.get_codeword()
    return code_dict

def invert_dict(dictionary):
    inv_dict = {}
    for x in dictionary.keys():
        inv_dict[(dictionary[x])] = x
    return inv_dict

def assign_code(code_dict, n):
    bcode = ''
    for x in n:
        bcode = bcode + code_dict[x]
    return bcode

def interpret_code(code_dict, bcode):
    string = ''
    i = 0
    #j = 1
    for j in range(len(bcode)):
            k = bcode[i:j]
            if k in code_dict:
                   string += code_dict[k]
                   #.keys()[code_dict.values().index(k)]
                   i = j
    return string


def binary2char(string):

    '''Returns character encoded version of a binary string.
       Note: padded to be divisible by 8 with pad length as first char.'''

    pad = 8 - len(string)%8
    string = string+pad*'0'
    out = str(pad)+''.join([chr(int(string[i:i+8],2))
                            for i in range(0,len(string),8)])
    return out

def char2binary(string):

    '''Returns binary string represented by a character string.
       Assumes first char represents number of pad bits.'''

    pad = int(string[0])
    out = ''.join([(10-len(bin(ord(char))))*'0' + bin(ord(char))[2:] for
                    char in string[1:]])
    return out[:-1*pad]


import pickle

def compression(infile, outfile):
    infile = open(infile, 'r')
    outfile = open(outfile, 'wb')
    #string = str_of_file(infile)
    string = infile.read()
    sym_prob_dict = calculate_probability(string)
    code_dict = dcode(sym_prob_dict)
    code = assign_code(code_dict, string)
    code = binary2char(code)
    pickle.dump(code_dict,outfile)
    outfile.write(code)
    infile.close()
    outfile.close()

def decompression(infile, outfile):
        infile = open(infile, 'rb')
        outfile = open(outfile, 'w')
        code_dict = pickle.load(infile)
        #char = str_of_file(infile)
        char = infile.read()
        code = char2binary(char)
        inv_code_dict = invert_dict(code_dict)
        string = interpret_code(inv_code_dict,code)
        outfile.write(string)
        infile.close()
        outfile.close()


def compression1(infile, outfile):
##        infile = open(infile, 'r')
        outfile = open(outfile, 'wb')
        string = str_of_file(infile)
        sym_prob_dict = calculate_probability(string)
        return HuffTree(sym_prob_dict)

            
            
        
            
            




                       
        
            
            
        

            
        

    



        
        
        
            
