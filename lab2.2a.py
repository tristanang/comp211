number = input("Enter a integer: ")
from math import *
process1 = sqrt(number)
process2 = int(process1)
epsilon = 0.00000000000000000000000000000000001
if process1-process2<epsilon:
    print True
else:
    print False
