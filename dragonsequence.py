def dragonsequence(n):
    memo={}
    memo[1]='L'
    def dragonhelper(x):
        for i in range(2,x+1):
            inversedragon=memo[i-1][::-1]
            inversedragon=inversedragon.replace('L','S')
            inversedragon=inversedragon.replace('R','D')
            inversedragon=inversedragon.replace('S','R')
            inversedragon=inversedragon.replace('D','L')
            memo[i]=memo[i-1]+'L'+inversedragon
        return memo[x]
    return dragonhelper(n)
