import re
from random import seed, randint
def rexp(str):
    str = str.lower()
    str = re.sub(' +', ' ', str)
    str = str.lstrip()
    return str.split(' ')

def GCF(x, y):
    if x > y:
        little = y
    else:
        little = x
    for i in range(1, little+1): #for loop prej 1 deri te me i vogli +1
        if ((x % i == 0) and (y % i == 0)): #operacioni modulo
            gcf = i
    print (gcf)
    return gcf

uInput = input("Enter input:")
vInput = rexp(uInput)
if(vInput[0] == 'gcf'):
    GCF(int(vInput[1]), int(vInput[2]))








