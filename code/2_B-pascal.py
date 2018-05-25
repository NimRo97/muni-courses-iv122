from math import factorial
from SVG import Svg

def basic_c(d, n):

    if n % 5 == 0:
        return "red"
    elif n % 5 == 1:
        return "blue"
    elif n % 5 == 2:
        return "green"
    elif n % 5 == 3:
        return "yellow"
    elif n % 5 == 4:
        return "cyan"

def bluish_c(d, n):
     return "rgb(0,0," + str(round(255 / d * (n % d)))+ ")"
    
def combination(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)

def generate_pascal(s):
    p = []
    for i in range(s):
        pc = [combination(i,j) for j in range(i+1)]
        p.append(pc)
    return(p)

def print_pascal(p, d, size, color_f):

    size = 10
    im = Svg("pascal.svg")

    for line in p:
        count = len(line)
        left_offset = count * size * -0.5
        for i in range(count):
            im.rectangle(left_offset + i * size, -(count - 1) * size,
            size, size, fill=color_f(d, line[i]))

    im.close()

def pascal(n, d, size=10, color_f=basic_c):
    print_pascal(generate_pascal(n), d, size, color_f)
