from QuickMult import quickMult

def quickPower(a, b, c):
    result = 1
    while b > 0:
        if (b & 1):
            result = quickMult(result, a, c)
        a = quickMult(a, a, c)
        b >>= 1
    return result