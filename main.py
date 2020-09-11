import random
from LargeNumber import GenerateLargeNumber
from QuickMult import quickMult
from QucikPower import quickPower
from MillerRabin import MillerRabinPrimeTest
from Generator import generators
from ExtendGCD import ExtendGCD


##系统参数Sys()
p = GenerateLargeNumber()
while not MillerRabinPrimeTest(p):
    p = GenerateLargeNumber()
G = range(1,p-1)
g = random.choice(generators(p))

##密码生成算法Gen()
x = random.choice(G)
pk = quickPower(g,x,p)
sk = x

##加密算法Enc()
m = 123
y = random.choice(G)
c1 = quickPower(g,y,p)
c2 = quickPower(pk,y,p)*m

##解密算法Dec()
newm = quickMult(c1,quickPower(c2,sk,p),p)
print(newm)



