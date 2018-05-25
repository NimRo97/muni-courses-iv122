def naive(a, n, k):
    return a ** n % k

def memory_efficient(a, n, k):
    r = 1
    while n > 0:
        r = a * r % k
        n -= 1
    return r

def efficient(a, n, k):
    r = 1
    a %= k
    while n > 0:
        if n % 2 == 1:
            r = (r * a) % k
        n //= 2
        a = a ** 2 % k
    return r
