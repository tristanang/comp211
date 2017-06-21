#See Hyung (Brian) Oh
#COMP_211_Final
#Dec 17 2016

import io
import random
import math
import collections
import heapq
import pickle

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

    def size(self):

        '''Returns the size of the tree'''

        if self.is_leaf():
            return 1
        else:
            return 1 + self.left.size() + self.right.size()

    def height(self):

        '''Returns the height of the tree'''

        if self.is_leaf():
            return 0
        else:
            return 1 + max((self.left.height(),self.right.height()))

    def lca(self,tree):

        '''Returns the least common answer of self and tree'''

        my_anc = self.list_of_ancestors()
        tree_anc = tree.list_of_ancestors()
        i=0
        while  i<len(my_anc) and i<len(tree_anc) and my_anc[i] == tree_anc[i]:
            i = i+1
        if my_anc[i-1] == tree_anc[i-1]:
            return my_anc[i-1]
        else:
            return None


    def contains(self,tree):

        '''Returns true iff self contains tree as a subtree'''

        if self == tree:
            return True
        elif self.is_leaf():
            return False
        else:
            return self.left.contains(tree) or self.right.contains(tree)

    def list_of_ancestors(self):
        '''Returns list of ancestors including self'''

        if self.is_root():
            return [self]
        else:
            return self.parent.list_of_ancestors() + [self]

    def list_of_leaves(self):

        '''Returns a list of all of the leaves of tree'''

        if self.is_leaf():
            return [self]
        else:
            return self.left.list_of_leaves()+self.right.list_of_leaves()

#Problem 1

class HuffmanTree(FullBinaryTree):

    def __init__(self,left=None,right=None,parent=None,symbol='',prob=0.0,code=''):
        FullBinaryTree.__init__(self,left,right,parent)
        self.symbol = symbol
        self.prob = prob
        self.code = code
        if left and right:
            self.prob = right.prob + left.prob            
        if left:
            left.code = '0'
        if right:
            right.code = '1'

    #a)
    def __cmp__(self,other):
        return cmp(self.prob,other.prob)

    #b)
##    def get_codeword(self):
##        lst = self.list_of_ancestors()[::-1][:len(self.list_of_ancestors())-1]
##        codeword = ''
##        for tree in lst:
##            codeword += tree.code
##        return codeword

    def get_codeword(self):
        if self.is_root():
            return ''
        else:
            return self.parent.get_codeword() + self.code            

    #c)
    def get_symbol(self,symbol):
        for tree in self.list_of_leaves():
            if symbol == tree.symbol:
                return tree
        return None

    def get_symbol2(self):
        return self.symbol


#Problem 2

#a)
def str_symbol(string):
    symbol_prob = {}
    lst_symbol = set(string)
    for letter in lst_symbol:
        n = string.count(letter)
        prob = float(n)/len(string) ##error
        symbol_prob[letter] = prob
    return symbol_prob

sp = str_symbol('oonn     ssssstttttaaarrrreeeee')

def tree(s,node):
    if node.get_symbol2():
        if not s:
            codes[node.get_symbol2()]="0"
        else:
            codes[node.get_symbol2()]=s
    else:
        tree(s+"0",node.left)
        tree(s+"1",node.right)

def HuffmanCode(symbol_prob):
    tree_lst = []
    for key in symbol_prob:
        tree_lst.append((symbol_prob[key],HuffmanTree(prob=symbol_prob[key],symbol=key)))
    heap = tree_lst
    heapq.heapify(heap)
    while len(tree_lst) > 1:
        min1 = heapq.heappop(heap)
        min2 = heapq.heappop(heap)
        newtree = (min1[0]+min2[0],HuffmanTree(min1[1],min2[1]))
        heapq.heappush(heap,newtree)
    bigtree = heap[0][1]
    codes = {}

    for key in symbol_prob:
        leaf = bigtree.get_symbol(key)
        print leaf
        code = leaf.get_codeword()
        codes[key] = code

    return codes
    

def encoding(infile,outfile):
    x = open(infile,'r')
    content = x.read()
    x.close()
    sp = str_symbol(content)                          
    dictionary = HuffmanCode(sp)
    temp = ''
    for c in content:
        code = dictionary[c]
        temp += code
    outfile = open(outfile,'wb')
    pickle.dump(dictionary, outfile)
    outfile.write(binary2char(temp))
    outfile.close()


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

def binary_to_str(binary,rev_dic):
    word = ''
    string = ''
    for num in binary:
        word += num
        if word in rev_dic:
            string += rev_dic[word]
            word = ''
    return string

def decoding(infile,outfile):
    compile_file = open(infile,'rb')
    decompile_file = open(outfile,'w')
    dictionary = pickle.load(compile_file)
    content = compile_file.read()
    binary = char2binary(content)
    rev_dic = {v:k for k,v in dictionary.iteritems()}
    string = binary_to_str(binary,rev_dic)
    decompile_file.write(string)
    compile_file.close()
    decompile_file.close()



    
                                  
        
            
        

#Problem 3
def n_file(n,alphabet,outfile):
    import random
    f = open(outfile,'w')
    s = ''
    while len(s) != n:            
        s += random.choice(alphabet)
    f.write(s)
    f.close()

#Problem 4
def identical_files(file1,file2):
    import filecmp
    return file.cmp(file1,file2)

#Problem 5
def str_entropy(string):
    prob_dict = prob(string)
    ent = 0
    for key in prob_dict:
        ent += (prob_dict[key]*(math.log((1/prob_dict[key]),10)))
    return ent

def str_prob(string):
    freq =  collections.Counter(string)
    length = float(len(string))

    for key in freq:
        freq[key]  = freq[key]/length
    return freq

#Problem 6

'''The results I got showed that the compression was better as the entropy was larger.''' 
    
        
        
        
        
            
            
        





a = HuffmanTree(symbol='A',code='0')
c = HuffmanTree(symbol='C',code='0')
t = HuffmanTree(symbol='T',code='1')
g = HuffmanTree(symbol='G',code='0')
ct = HuffmanTree(left=c,right=t,code='1')
ctg = HuffmanTree(left=g,right=ct,code='1')
root = HuffmanTree(left=a,right=ctg)
##print a.get_parent()
##print c.get_parent()
##print t.get_parent()
##print g.get_parent()
##print a.get_codeword()
##print t.get_codeword()
##print root.get_symbol('A')
##print root.get_symbol('A')



            
        
