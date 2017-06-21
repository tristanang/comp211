# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer

def inttolist(n):
    b = str(n)
    c = []
    for digit in b:
        c.append (int(digit))
    return c

def rounddown(x):
    x = str(x)
    return 10 ** (len(x)-1)

def tidynumber(n):
    number = str(n)
    if len(number) == 1:
        return True
    first = int(number[0])
    second = int(number[1])
    if first > second:
        return False
    else:
        recurse = int(number[1:])
        return tidynumber(recurse)

def sdc(n):
    stringed = str(n)
    if len(stringed) == 1:
        return True
    elif stringed[0] == stringed[1]:
        return sdc(int(stringed[1:]))
    else:
        return False
   

def tidyloop(n):
    count = n
    array = inttolist(n)
    if sdc(n):
        return n
    index = 0
    while array[index]<=array[index+1]:
        index += 1
        if index == len(array) - 1:
            return n
    array[index] -= 1
    for i in range(index+1,len(array)):
        array[i] = 9
    while array[0] == 0:
        array = array[1:]
    answer = ""
    for i in range(0,len(array)):
        answer += str(array[i])
        integer = int(answer)
    return tidyloop(integer)
        
    
    
        
        




def tidyloopshit(n):
    count = n
    stringed = str(n)
    if sdc(n):
        return n
    while not tidynumber(count):
        count -= 1
    return count


    

    
for i in xrange(1, t + 1):
    n = int(raw_input())
    m = tidyloop(n)
    print "Case #{}: {}".format(i, m)
  # check out .format's specification for more formatting options
