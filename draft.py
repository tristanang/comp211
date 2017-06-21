def read_roll(fasta_file,lst2):

    sequence_list = []
    file_in = open(fasta_file, 'r')
    line = file_in.readline().strip('Picture of')
    while line != '':
        placeholder=line.split('\t')
        sequence_list.append(placeholder[0])
        line = file_in.readline().strip('Picture of')
    file_in.close()
    sequence_list2=[]
    file_in=open(lst2,'r')
    line = file_in.readline().strip('Picture of')
    while line != '':
        placeholder=line.split('\t')
        sequence_list2.append(placeholder[0])
        line = file_in.readline().strip('Picture of')
    file_in.close()
    for element in sequence_list:
        if element in sequence_list2:
            print element
    
