from random import uniform

def leibniz(accuracy):
    return 4 * sum([(- 1) ** x / (2 * x + 1) for x in range(accuracy)])

def archimedes(accuracy):
    
    a, b = 2, 4
    for n in range(accuracy):
        a = 2 - 2 * ((1 - a / 4) ** 0.5)
        b *= 2

    return b * (a ** 0.5) / 2
    
def monte_carlo_random(accuracy):
    c = 0
    for n in range(accuracy):
        if (uniform(0, 1) ** 2 + uniform(0, 1) ** 2) ** 0.5 <= 1:
            c += 1
    return 4 * c / accuracy

def monte_carlo(accuracy):
    c = 0
    for i in range(accuracy + 1):
        for j in range(accuracy + 1):
            if ((i / accuracy) ** 2 + (j / accuracy) ** 2) ** 0.5 <= 1:
                c += 1
    return 4 * c / accuracy / accuracy
