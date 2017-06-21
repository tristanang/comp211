def f():
    global contactbook
    contactbook={}
    name = raw_input(' name or q')
    if name == 'q':
            quit
    else:
        prenumber = raw_input(' number please')
        number=int(prenumber)
        contactbook[name]=number
        print contactbook
        f()

def g():
    request = raw_input('which fool you want')
    return contactbook[request]
    if request == 'q':
        quit
    else:
        g()

hi=raw_input('input or output')
if hi == input:
    f()
elif hi == output:
    g()

