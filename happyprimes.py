def happyprimelist(n):
    lst=[]
    i=2
    while i<n:
        if isprime(i) and ishappy(i):
            lst.append(i)
        i=i+1
    return lst

def isprime(x):
    from math import sqrt
    for j in range(2,int(sqrt(x)+1)):
        if x % j == 0:
            return False
    return True

def ishappy(x):
    memo=[]
    def ishappyhelper(x):
        
        if x == 1:
            return True
        elif x in memo:
            return False
        else:
            memo.append(x)
            return ishappyhelper(sumofsquareofdigits(x))
    return ishappyhelper(x)

def sumofsquareofdigits(n):
    if n == 0:
        return 0
    return (n%10)**2 + sumofsquareofdigits(n//10) 
