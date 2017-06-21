def alpha(N):
    prod = 1
    for i in range(1,2**N+1):
        prod = prod*2
    return prod

def beta(N):
    if N==0:
        return 2
    else:
        return (beta(N-1))**2
