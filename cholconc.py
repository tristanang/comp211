def conc(chol,dppc):
    nperchol=8.
    nperlipid=12.
    total=chol+dppc
    total = float(total)
    print total
    concentration = chol/total
    print "concentration="+str(concentration)
    dppcmass=734.039
    cholmass=386.65
    dppctot=dppc*dppcmass
    choltot=chol*cholmass
    tot=dppctot+choltot
    print "massconc="+str(choltot/tot)


    
    
