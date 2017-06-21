def fib(n):
    memo={}
    memo[1]=memo[2]=1
    memo[0]=0
    def fibhelper(n):
        for i in range(2,n+1):
            memo[i]=memo[i-1]+memo[i-2]
        return memo[n]
    return fibhelper(n)
