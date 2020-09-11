def quickMult(a, b, c):
    result = 0
    while b > 0:
        if b & 1:
            result = (result + a) % c
        a = (a + a) % c
        b >>= 1
    return result