#Possible solutions to COMP 211 (Fall 2016) Lab 4
#Author: Danny Krizanc
#Oct 2016

#Problem 2

def phonebook_entry(phonebook):
    '''Adds entries to phonebook (dictionary) and returns new phonebook'''
    
    name = raw_input('Enter a name (or q to quit): ')
    while name != 'q':
        phone = raw_input('Phone number: ')
        phonebook[name] = phone
        name = raw_input('Enter a name (or q to quit): ')
    return phonebook

def phonebook_initiate():
    '''Initiates a new phonebook starting with an empty dictionary'''
    
    return phonebook_entry({})

def phonebook_query(phonebook):
    '''Given phonebook, queries user for a name and returns phone number'''

    name = raw_input('Whose phone number do you want: ')
    print name+"'s phone number is",phonebook[name]

def main_phonebook():
    '''Tests the above'''
    
    phonebook = phonebook_initiate()
    phonebook_query(phonebook)

#Problem 5 (continuation of Problem 2 with files)

def phonebook_loop(task):
    '''Performs phonebook file task as given by task'''

    if task == '1':
        phonebook_file = raw_input("Enter the a name for your new phonebook: ")
        phonebook = phonebook_initiate()
        p_file = open(phonebook_file,'w')
        p_file.write(str(phonebook))
        p_file.close()
    elif task == '2':
        phonebook_file = raw_input("Phonebook file to added to: ")
        p_file = open(phonebook_file, 'r+')
        phonebook = eval(p_file.read()) #restore dictionary using eval - use pickle?
        phonebook = phonebook_entry(phonebook)
        p_file.seek(0)
        p_file.write(str(phonebook))
        p_file.close()
    else:
        phonebook_file = raw_input("Phonebook file to retrieve number from: ")
        p_file = open(phonebook_file, 'r')
        phonebook = eval(p_file.read())
        phonebook_query(phonebook)
        p_file.close()
        
def main_phonebook_file():
    '''Input loop for phonebook program'''

    while True:
        task = raw_input('''
What would you like to do? Enter
1 to start a new phonebook
2 to add to a current phonebook
3 to retrieve a phone number
q to quit
''')
        if task == 'q': break
        phonebook_loop(task)
    print "Goodbye"


#Problem 3

def sub_cipher(key,plaintext):
    '''Return ciphertext of subsitution cipher given key and plaintext'''

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_dict = dict(zip(alphabet,key))
    key_dict[' '] = ' '
    ciphertext = ''
    for ch in plaintext:
        ciphertext = ciphertext + key_dict[ch]
    return ciphertext

def main_cipher():
    '''Test substitution cipher'''

    key = raw_input('Please enter your key: ')
    plaintext = raw_input('Please enter your plain text: ')
    print "The cipher text is:", sub_cipher(key,plaintext)

#Problem 5 (continuation of Problem 3 using files)

def main_cipher_files():
    '''Performs substitution cipher on user provided file with user provided
       key. Outputs result to user provided file.'''

    key = raw_input('Please enter your key: ')
    in_file = raw_input('Please enter name of input file: ')
    out_file = raw_input('Please enter name of output file: ')
    in_f = open(in_file,'r')
    out_f = open(out_file,'w')
    for ln in in_f:
        ln = ln.rstrip('\n')
        cipherln = sub_cipher(key,ln)
        out_f.write(cipherln+'\n')
    in_f.close()
    out_f.close()
    
    
#Problem 4. Note: For Excel to open correctly you must assume that
#the gene name does not contain any commas!

def countACGT(fasta,csv):
    '''Count ACGT in input fasta file and store result in csv file'''
    
    fasta = open(fasta,'r')
    csv = open(csv,'w')
    genes = fasta.read().split('>') #Reads all of file at once!
    for gene in genes[1:]: #Note: before first '>' is an empty gene
        gene_info = gene.split('\n',1) # split off first line of gene
        gene_name = gene_info[0]
        a,c,g,t = gene_info[1].count('A'),gene_info[1].count('C'),\
                  gene_info[1].count('G'),gene_info[1].count('T')
        csv.write(gene_name+','+str(a)+','+str(c)+','+str(g)+','+str(t)+'\n')
    fasta.close()
    csv.close()

def main_countACGT():
    '''Test countACGT function.'''

    in_file = raw_input('Input fasta file: ')
    out_file = raw_input('Output csv file: ')
    countACGT(in_file,out_file)

    
    
        



    
