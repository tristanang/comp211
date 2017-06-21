def sum_digits(n,b):
    if n==0:
        return 0
    else:
        return n%b + sum_digits(n//b,b)
