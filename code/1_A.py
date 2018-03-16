from math import ceil


def div_count(n):    
    count = 0   
    for i in range(1, n):
        if n % i == 0:
            count += 1               
    return count

def max_div_count(n):
    return max([i for i in range(n+1)], key = lambda x:div_count(x))

def max_div_count_count(n): #7560 aj 9240
    return [i for i in range(n+1)].count(max_div_count(n))


def sec_powers():
    return [i**2 for i in range(1,32)]

def is_sum_of_pow():
    return [i+j+k for i in sec_powers() \
            for j in sec_powers() for k in sec_powers()]

def sum_sec_pow(): #ma byt 200
    return [i for i in range]


def collatz(n):
    count = 0
    while n != 1:
        count += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
    return count

def max_collatz(n):
    return max([i for i in range(1, n+1)], key = lambda x:collatz(x))



def is_prime(n):
    
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True

def has_3(n):
    return n % 10 == 3 or n // 100 == 3 or n // 10 % 10 == 3

def sum_prime_no3():
    return sum([i for i in range(1000) if is_prime(i) and not has_3(i)])


def nsd(a,b):
    if b == 0:
        return a
    else:
        return nsd(b, a % b)

def sequence():
    a, b = 1, 1
    while b <= 1000000:
        a, b = b, a + b + nsd(a, b)
    return b
    
