def fib(n):
    memo={}
    memo[1]=memo[2]=1
    memo[0]=0
    def fibhelper(n):
        if n in memo:
            return memo[n]
        else:
            memo[n]=fibhelper(n-1)+fibhelper(n-2)
            return memo[n]
    return fibhelper(n)
