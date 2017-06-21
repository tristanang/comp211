cipher=raw_input('cipher fool:')
scrambler={}
buttstuff=''
count=0
for a in 'abcdefghijklmnopqrstuvwxyz': 
    scrambler[a]=cipher[count]
    count = count + 1
plaintext=raw_input('plain text fool:')
for i in plaintext:
    if i not in scrambler:
        buttstuff += i
    else:
        buttstuff += scrambler[i]
print buttstuff
    

