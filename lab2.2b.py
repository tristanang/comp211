x = input("Enter an integer: ")
if abs(x)<100:
    print 0
else:
    y = x//100
    last_digit = int(repr(y)[-1])
    print last_digit
