# Tristan Ang Tze Heng
# Nov 2016

import heapq
import zlib
import pickle
import string
import math
import os


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
        if left and right: #probability of parent is sum of probability of children
            self.prob = right.prob + left.prob            
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
            return '' #root needs no code (since it is always traversed)
        else:
            return self.parent.get_codeword() + self.code
        
    def get_symbol(self,symbol):
        if self.is_leaf() and self.symbol == symbol: #only leaves has symbols
            return self
        elif self.is_leaf(): #if self is only a single node and self.symbol!=symbol, clearly leaf with symbol is not in this 'tree'
            return None
        else:
            return self.left.get_symbol(symbol) or self.right.get_symbol(symbol) #traverse both sides of tree

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
    if len(heap) == 1:
        return heap[0][1]
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

def invertdict(memo): #inverts dictionary
    return dict((v,k) for k, v in memo.iteritems())
    
def compression(infile,outfile):
    infile = open(infile,'r')
    instring = infile.read()
    if instring == '': ## exception to end code when given empty file
        outfile = open(outfile,'w')
        outfile.close()
        return
    infile.close()
    sptuple = sptuplegen(instring) 
    root = huffmanroot(sptuple)
    if root.is_leaf(): #exception when there is only one character occuring (All As) Creates dictionary with one entry
        memo = {}
        memo[root.symbol] = '0' #will work if is its 1 too
    else:
        memo = dictgen(root)
    outstring = ''
    for char in instring:
        outstring += memo[char]
    convert = bin2char(outstring)
    outfile = open(outfile,'wb')
    pickle.dump(memo, outfile)
    outfile.write(convert)
    outfile.close()

def decompression(infile,outfile):
    infile = open(infile,'rb')
    try:
        '''so that code igores / is able to deal with empty files'''
        memo = pickle.load(infile) #unpickles memo
    except:
        outfile = open(outfile,'w')
        outfile.close()
        return
    memo = invertdict(memo)
    instring = infile.read()
    infile.close()
    convert = char2bin(instring)
    outstring = interpret(convert,memo)
    outfile = open(outfile,'w')
    outfile.write(outstring)
    outfile.close()
    
def interpret(strng,memo):
    ''' Given string and a key, converts string using key'''
    outstring = ''
    interpret = ''
    for i in range(len(strng)):
        interpret += strng[i]
        if interpret in memo:
            outstring += memo[interpret]
            interpret = ''
    return outstring
    
def bin2char(strng):
    ''' binary to char'''
    iterations = len(strng)/8
    remainder = len(strng)%8 ## string not in multiple of 8 therefore we do not convert some binary into char
    outstring = str(strng[0:remainder])+'>' ##marks the file such that we know before '>' the binary are not chars
    j = remainder
    for i in range(iterations):
        outstring += chr(int(strng[j:j+8],2)) ##reads 8 bits at a time
        j += 8
    return outstring

def char2bin(strng):
    '''char to binary'''
    lst = strng.split('>',1) ##separates the part before '>' which we know is not char
    outstring = lst[0]
    for char in lst[1]:
        transient=bin(ord(char))[2:]
        while len(transient) != 8: ##adds the leading zeros back
            transient = '0' + transient
        outstring += transient
    return outstring
        
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
    return string1 == string2 and checksum(file1) == checksum(file2) ##compares string representation and md5 of files
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

def entropy(strng):
    '''using formula in reading'''
    sptuple = sptuplegen(strng)
    if len(strng) == 0:
        return 0.
    total = 0.
    entropy = 0.
    for tup in sptuple:
        total += tup[0]
    for tup in sptuple:
        entropy += (tup[0]/total)*(math.log((total/float(tup[0])),2))
    return entropy

################
###QUESTION 6###
################

def file2string(fp):
    fp = open(fp,'r')
    strng = fp.read()
    fp.close()
    return strng

def string2file(strng,outfile):
    fp = open(outfile,'w')
    fp.write(strng)
    fp.close()
    
def main6(file1='sample.txt',file2='fasta.txt',file3='random.txt',file4='allAs.txt',file5='empty.txt'):
    compression(file1,'1.com')
    compression(file2,'2.com')
    compression(file3,'3.com')
    compression(file4,'4.com')
    compression(file5,'5.com')
    string2file(zlib.compress(file2string(file1)),'1.zlib')
    string2file(zlib.compress(file2string(file2)),'2.zlib')
    string2file(zlib.compress(file2string(file3)),'3.zlib')
    string2file(zlib.compress(file2string(file4)),'4.zlib')
    string2file(zlib.compress(file2string(file5)),'5.zlib')
    assert testcomp(file1)
    assert testcomp(file2)
    assert testcomp(file3)
    assert testcomp(file4)
    assert testcomp(file5)
    print 'all files compared and passed'
    print ['File Name ','Size ','Compressed Size','Zip Size','    Entropy   ']
    print [file1,str(int(os.path.getsize(file1))),'     '+str(int(os.path.getsize('1.com')))+'     ','  '+str(int(os.path.getsize('1.zlib')))+' ',str(entropy(file2string(file1)))+'0']
    print [file2+' ',str(int(os.path.getsize(file2)))+' ','     '+str(int(os.path.getsize('2.com')))+'      ','  '+str(int(os.path.getsize('2.zlib')))+'  ',str(entropy(file2string(file2)))+'0']
    print [file3,str(int(os.path.getsize(file3))),'     '+str(int(os.path.getsize('3.com')))+'     ','  '+str(int(os.path.getsize('3.zlib')))+' ',str(entropy(file2string(file3)))+'0']
    print [file4+' ',str(int(os.path.getsize(file4))),'     '+str(int(os.path.getsize('4.com')))+'      ','  '+str(int(os.path.getsize('4.zlib')))+'    ',str(entropy(file2string(file4)))+'00000000000']
    print [file5+' ',str(int(os.path.getsize(file5)))+'    ','     '+str(int(os.path.getsize('5.com')))+'         ','  '+str(int(os.path.getsize('5.zlib')))+'     ',str(entropy(file2string(file5)))+'00000000000']

'''
['File Name ', 'Size ', 'Compressed Size', 'Zip Size', '    Entropy   ']
['sample.txt', '46975', '     30284     ', '  19042 ', '4.709685905670']
['fasta.txt ', '6969 ', '     2681      ', '  2022  ', '2.051983183730']
['random.txt', '20000', '     12631     ', '  12690 ', '4.753764444560']
['allAs.txt ', '20000', '     2524      ', '  43    ', '0.000000000000']
['empty.txt ', '0    ', '     0         ', '  8     ', '0.000000000000']

Looking at the entropies of sample.txt, fasta.txt, allAs.txt, and random.txt, it seems that the lower the entropy,
the better both my algorithm and zlib are able to compress files. Zlib ofcourse does better because its
more developed. This shouldn't be suprising; if an algorithm I coded in 2 days could beat zlib it would
mean zlib is really bad. The zipsize for empty.txt is strange, I would expect them to handle that simple
exception as I did.
My algorithm did best on fasta.txt and allAs.txt, because there was a high probabilty of only a few characters. Similarly,
it did worst on sample.txt and random.txt where the probabilities of various characters appearing are relatively
uniform.
'''
