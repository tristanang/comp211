def circle(x,y,r=1.0):
    x = float(x)
    y = float(y)
    r = float(r)
    if x**2 + y**2 == r**2:
        return True
    else:
        return False
