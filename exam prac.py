def distinct_pow(N):
    lst=[]
    for i in range(2,N+1):
        for j in range(2,N+1):
            if i**j not in lst:
                lst.append(i**j)
    return lst

def distinct_pows(N):
    from sets import Set
    s=Set([])
    for i in range(2,N+1):
        for j in range(2,N+1):
            if i**j not in s:
                s.add(i**j)
    return len(s)
