def ExtendGCD(a,b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, q = ExtendGCD(b, a % b)
        x, y = y, (x - (a // b) * y)
        return x, y, q
