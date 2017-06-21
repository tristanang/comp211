k = [15,28,16,14,14,13,15,15]

def massspect(n,fragment):
    n,m = mspect1(n,fragment),mspect2(n,fragment)
    print "Front="+str(n)
    print "Back="+str(m)

def mspect1(n,fragment):
    working = 0
    index = 0
    while working != fragment:
        working += n[index]
        index += 1
        if index == len(n):
            return "Error"
    return n[0:index]

def mspect2(n,fragment):
    working = 0
    index = len(n) - 1
    
    while working != fragment:
        working += n[index]
        index -= 1
        if index == -1:
            return "Error"
    return n[index+1:]

def arraysum(lst):
    if lst == []:
        return 0
    summ = 0
    for i in range(0,len(lst)):
        summ += lst[i]
    return summ

def emassspect(n,fragment):
    index = 0
    lst = []
    for i in range(0,len(n)):
        lst.append(n[i])
        if arraysum(lst) > fragment:
            lst = lst[1:]
        if arraysum(lst) == fragment:
            return lst
    print lst
    return "Error"
        
            
    
        

    
    
