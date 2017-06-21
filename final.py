# Tristan Ang Tze Heng
# Nov 2016

import heapq
import zlib
import itertools
import array
import pickle
import string


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
        if left:
            left.parent = self
        if right:
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
        return not self.parent

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
################
###QUESTION 1###
################
    
class HuffmanTree(FullBinaryTree):
    def __init__(self,symbol,prob=0,left=None,right=None,code=None,parent=None):
        self.symbol = symbol
        FullBinaryTree.__init__(self,left,right,parent)
        self.prob = prob
        if left and right:
            self.prob = right.prob + left.prob    
        self.code = code        
        if left:
            left.code = '0'
        if right:
            right.code = '1'
            
    def __cmp__(self,other):
        '''Returns comparison of self prob and other prob'''
        if self.prob > other.prob:
            return 1
        elif self.prob == other.prob:
            return 0
        else:
            return -1

    def get_codeword(self):
        if self.is_root():
            return '' 
        else:
            return self.parent.get_codeword() + self.code
        
    def get_symbol(self,symbol):
        if self.is_leaf() and self.symbol == symbol:
            return self
        elif self.is_leaf():
            return None
        else:
            return self.left.get_symbol(symbol) or self.right.get_symbol(symbol)

o = HuffmanTree('o',2)
n = HuffmanTree('n',2)
on = HuffmanTree('placeholder',0,o,n)
space = HuffmanTree(' ',5)
onspace = HuffmanTree('placeholder',0,on,space)
s = HuffmanTree('s',5)
t = HuffmanTree('t',5)
st = HuffmanTree('placeholder',0,s,t)
onspacest = HuffmanTree('placeholder',0,onspace,st)
a = HuffmanTree('a',3)
r = HuffmanTree('r',4)
ar = HuffmanTree('placeholder',0,a,r)
e = HuffmanTree('e',5)
are = HuffmanTree('placeholder',0,ar,e)
onspacestare = HuffmanTree('placeholder',0,onspacest,are)

def testHuffTree():
    o = HuffmanTree('o',2)
    n = HuffmanTree('n',2)
    on = HuffmanTree('placeholder',0,'2',o,n)
    space = HuffmanTree(' ',5)
    onspace = HuffmanTree('placeholder',0,'2',on,space)
    s = HuffmanTree('s',5)
    t = HuffmanTree('t',5)
    st = HuffmanTree('placeholder',0,'2',s,t)
    onspacest = HuffmanTree('placeholder',0,'2',onspace,st)
    a = HuffmanTree('a',3)
    r = HuffmanTree('r',4)
    ar = HuffmanTree('placeholder',0,'2',a,r)
    e = HuffmanTree('e',5)
    are = HuffmanTree('placeholder',0,'2',ar,e)
    onspacestare = HuffmanTree('placeholder',0,'2',onspacest,are)
    assert onspacestare.get_symbol('o') == o
    assert onspacestare.get_symbol('n') == n
    assert onspacestare.get_symbol(' ') == space
    print 'passed all tests'
    return onspacestare

################
###QUESTION 2###
################

def sptuplegen(instring): ## generate sptuple from infile ##sptuple=symbol-probability tuple
    sptuple = []
    for char in string.printable:
        if instring.count(char) != 0:
            sptuple.append((instring.count(char),char))
    return sptuple

def init_leaves(sptuple):
    lst_leaves = []
    for element in sptuple:
        lst_leaves.append((element[0],HuffmanTree(element[1],element[0])))
    return lst_leaves   

def huffmanroot(sptuple): ##returns root of huffman tree
    heap = init_leaves(sptuple)
    heapq.heapify(heap)
    s = heapq.heappop(heap) #s=smallest
    ss = heapq.heappop(heap) #ss=secondsmallest
    join = (s[0]+ss[0],HuffmanTree(s[1].symbol+ss[1].symbol,s[0]+ss[0],s[1],ss[1]))
   
    while len(heap) > 1:
        s = heapq.heappushpop(heap,join)
        ss = heapq.heappop(heap)
        join = (s[0]+ss[0],HuffmanTree(s[1].symbol+ss[1].symbol,s[0]+ss[0],s[1],ss[1]))
    root = HuffmanTree(heap[0][1].symbol+join[1].symbol,heap[0][0]+join[0],heap[0][1],join[1])
    return root

def dictgen(root): #generate dictionary from root        
    leaves = root.list_of_leaves()
    memo = {}
    for leaf in leaves:
        memo[leaf.symbol] = leaf.get_codeword()
    return memo

def invertdict(memo):
    return dict((v,k) for k, v in memo.iteritems())
    
def compression(infile,outfile):
    infile = open(infile,'r')
    instring = infile.read()
    infile.close()
    sptuple = sptuplegen(instring)
    root = huffmanroot(sptuple)
    memo = dictgen(root)
    outstring = ''
    for char in instring:
        outstring += memo[char]
    convert = binarytobase64(outstring)
    outfile = open(outfile,'w')
    pickle.dump(memo, outfile)
    outfile.write(convert)
    outfile.close()

def decompression(infile,outfile):
    infile = open(infile,'r')
    memo = pickle.load(infile)
    memo = invertdict(memo)
    instring = infile.read()
    infile.close()
    convert = base64tobinary(instring)
    outstring = interpret(convert,memo)
    outfile = open(outfile,'w')
    outfile.write(outstring)
    outfile.close()
    
def interpret(strng,memo):
    outstring = ''
    interpret = ''
    for i in range(len(strng)):
        interpret += strng[i]
        if interpret in memo:
            outstring += memo[interpret]
            interpret = ''
        if strng[i] == '<':
            return outstring+strng[i+1:]
    if interpret == '':
        return outstring
    else:
        return outstring+'<'+interpret

def binarytobase64(strng):
    return interpret(strng,invertdict(base64memo()))

def base64tobinary(strng):
    return interpret(strng,base64memo())
    
def base64memo(): ##6bits
    memo ={}
    lst = binary64lst()
    for i in range(64):
        memo[string.printable[i]]=lst[i]
    return memo

def binary64lst():
    lst = []
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        for f in range(2):
                            lst.append(str(a)+str(b)+str(c)+str(d)+str(e)+str(f))
    return lst

    

'''
Why binary string created larger than original file?
This is because it was not written in binary representation but used ascii representation for 1s and 0s.
'''
################
###QUESTION 3###
################

def rand_file(fp,n,symbolset='abcdefghijklmnopqrstuvwxyz '): #adapted from random dna code in lab
    import random
    fp = open(fp,'w')
    outstring = ''
    for i in range(n):
        outstring = outstring + random.choice(symbolset)
    fp.write(outstring)
    fp.close()

################
###QUESTION 4###
################

def file_comparison(file1,file2):
    #import filecmp
    f1 = open(file1,'r')
    string1 = f1.read()
    f1.close()
    f2 = open(file2,'r')
    string2 = f2.read()
    f2.close()
    return string1 == string2 and checksum(file1) == checksum(file2)
    #return filecmp.cmp(file1,file2)

def checksum(f): ##googled
    import hashlib
    md5 = hashlib.md5()
    md5.update(open(f).read())
    return md5.hexdigest()

def testcomp(infile): ##test compression
    compression(infile,'middle')
    decompression('middle','final')
    return file_comparison(infile,'final')

################
###QUESTION 5###
################

#def entropy(

def fuck(binary):
    test = binary
    test1 = bin(int(test,2))
    assert test1[2:] == test

##fuck
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

sptuple = [(2,'o'),(2,'n'),(5,' '),(5,'s'),(5,'t'),(3,'a'),(4,'r'),(5,'e')]
#instring = compression('mitochondrial_dna.fasta','fds')
root = huffmanroot(sptuple)

'''
junk

from array import *

bin_array = array('B')

bin_array.append(int('011',2))
bin_array.append(int('010',2))
bin_array.append(int('110',2))

f = file('binary.mydata','wb')
bin_array.tofile(f)
f.close()
'''

#bit = binary2char(outstring)
    #return outstring
    #convert1 = int(outstring,2)
    #convert2 = hex(convert1)[2:]
    #assert bin(int(convert2, 16))[2:] == outstring
#bin(int("abc123efff", 16))[2:]
