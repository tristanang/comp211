class Complex(object):
    '''Implement complex numbers'''
    def __init__(self,r,i):
        
        '''Constructor for Complex'''
        self.r=r
        
        self.i=i
    def __str__(self):
        '''To string'''
        return str(self.r)+'+'+str(self.i)+'j'
    def __repr__(self):
        '''Representation'''
        return 'Complex('+str(self.r)+','+str(self.i)+')'
    def __eq__(self,other):
        '''Implements =='''
        return self.r==other.r and self.i==other.i
