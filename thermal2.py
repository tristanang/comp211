import math

def within(N):
    lower = int(0.49*N)
    upper = int(0.51*N)
    total = 0.
    for H in range(lower,upper+1):
        total += int(1000*(math.factorial(N)/(math.factorial(H)*math.factorial(N-H)))*(math.pow(0.5,N)))
    print total
    
