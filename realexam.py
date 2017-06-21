def f(n,m):
    val = 1
    for i in range(m):
        val = val*n
    return val

def ptriple(n):
    for a in range(1,n/2+1):
        '''triangle inequality states a max = n/2'''
        for b in range(a+1,n/2):
            '''same max for b but start at a+1'''
            c=n-(a+b) ##
            assert a+b+c==n
            assert a>0 and b>0 and c>0
            if a**2+b**2==c**2 and c>0:
                return a,b,c
    #return False
