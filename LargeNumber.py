import random

def GenerateLargeNumber(keysize=13):
    number = random.randrange(2 ** (keysize - 1 ),2 ** keysize)
    return  number