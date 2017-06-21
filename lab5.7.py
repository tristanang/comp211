def exactly_k(string,ch,k):
    '''Returns True if the character ch appears exactly k times in string'''
    if string == '' and k==0:
        return True
    elif string == '' and k!=0:
        return False
    elif string[0] == ch:
        return exactly_k(string[1:],ch,k-1)
    else:
        return exactly_k(string[1:],ch,k)
