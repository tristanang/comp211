def happylist(n):
    lst=[1]
    def sumofsquareofdigits(n):
        if n == 0:
            return 0
        return (n%10)**2 + sumofsquareofdigits(n//10)
    def ishappy(x):
        memo=[]
        def ishappyhelper(x):
        
            if x == 1:
                return True
            elif x in lst:
                return True
            elif x in memo:
                return False
            else:
                memo.append(x)
            return ishappyhelper(sumofsquareofdigits(x))
        return ishappyhelper(x)
    lst=[1]
    i=2
    while i<=n:
        if ishappy(i):
            lst.append(i)
        i=i+1
    return lst


  
