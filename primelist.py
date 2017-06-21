def primelist(n):
    lst=[2]
    def isprime(x):
        for j in range(len(lst)):
            if lst[j]*lst[j] <= x:
                if x % lst[j] == 0:
                    return False
        return True
    i=3
    while i<=n:
        if isprime(i):
            lst.append(i)
        i=i+1
    return lst
    

"""
create a list (lst) with one elemement (2 - 1st prime number)
set index i to 3
while the last number (element) in the lst is smaller than n
    is the 

"""
