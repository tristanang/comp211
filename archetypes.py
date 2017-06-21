def f(csv):

    stream = []
    csv = open(csv,'r')
    genes = csv.read().split(';')
    
    for gene in genes: 
        stream.append(gene.split('\n'))

    flattened = [val for sublist in stream for val in sublist]
    remove_empty = []
    
    for element in flattened:
        if element != '':
            remove_empty.append(element)

    bargain = []
    comfort = []
    planner = []
    foodie = []
    spur = []
    explorer = []

    
        
##    b,c,e,f,p,s = 0,0,0,0,0,0
    current = []
    arche = remove_empty[0]
    current.append(arche)
    
    

    for element in remove_empty[1:]:
        
        
        if element == 'Explorer' or element == 'Planner' or element == 'Bargain Hunters' or element == 'Foodie' or element == 'Comfort Seeker' or element == 'Spur of the Moment':
            if arche == 'Explorer':
                explorer.append(current)
                current = []
            if arche == 'Planner':
                planner.append(current)
                current = []
            if arche == 'Bargain Hunters':
                bargain.append(current)
                current = []
            if arche == 'Comfort Seeker':
                comfort.append(current)
                current = []
            if arche == 'Spur of the Moment':
                spur.append(current)
                current = []
            if arche == 'Foodie':
                foodie.append(current)
                current = []

            arche = element
            
        current.append(element)

    bargain.append(current)       

    return bargain,comfort,planner,foodie,spur,explorer
    
bargain,comfort,planner,foodie,spur,explorer = f('WW Survey Results.csv')            

def checkout_bool(person):
    if 'Self-service checkout errors' in person or 'Checkout that is able to scan and display the prices for all items in one go, instead of having to scan the products individually' in person or 'Takes a long time to queue and checkout' in person:
        return True
    else:
        return False
        
def checkouter():

    num_bargain = len(bargain)
    num_comfort = len(comfort)
    num_planner = len(planner)
    num_foodie = len(foodie)
    num_spur = len(spur)
    num_explorer= len(explorer)

    summ = 0.
    
    for person in bargain:
        if checkout_bool(person):
            summ += 1.
    
    p_bargain = summ/num_bargain

    summ = 0.
    
    for person in comfort:
        if checkout_bool(person):
            summ += 1.
    
    p_comfort = summ/num_comfort

    summ = 0.
    
    for person in planner:
        if checkout_bool(person):
            summ += 1.
    
    p_planner = summ/num_planner

    summ = 0.
    for person in foodie:
        if checkout_bool(person):
            summ += 1.
    p_foodie = summ/num_foodie

    summ = 0.
    for person in spur:
        if checkout_bool(person):
            summ += 1.
    p_spur = summ/num_spur

    summ = 0.
    for person in explorer:
        if checkout_bool(person):
            summ += 1.
    p_explorer = summ/num_explorer
    
    return p_bargain,p_comfort,p_planner,p_foodie,p_spur,p_explorer
    
    
            



##        gene_info = gene.split('\n',1)  
##        lst.append((gene_info[0],gene_info[1].replace('\n','')))
##        #appends tuple to list. replace module removes all '\n'
##    return lst
