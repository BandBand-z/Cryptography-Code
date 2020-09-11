import random
from QucikPower import quickPower

##米勒拉宾
def MillerRabinPrimeTest(n):
    if n==2:
        return False
    if n<2:
        return False
    if n & 0:
        return False
    d = n-1
    s = 0
    a = random.randint(1,n-1)
    while (d & 1) == 0:
        s += 1
        d >>= 1

    x = quickPower(a,d,n)
    for i in range(s):
        newX = quickPower(x,2,n)
        if newX == 1 and x !=1 and x!= n-1:
            return  False
        x = newX

    if x!=1:
        return False
    return True