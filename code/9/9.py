from random import randint
#matplotlib

def analyse():
    for i in range(1, 8):
        res = [0]*6
        f = open("random"+str(i)+".txt", "r")
        numbers = map(lambda x: int(x), f.readline().split(" "))
        for n in numbers:
            res[n-1] += 1
        print("file: random "+str(i))
        for i in range(6):
            print(i+1,":",res[i])

def bayes_simulation(n, x):
    count = 0
    count_fake = 0
    count_real = 0
    for i in range(100000):
        if randint(1, n) == 1:
            count += 1
            count_fake += 1
        else:
            holds = True
            for i in range(x):
                if randint(1, 6) != 1:
                    holds = False
            if holds:
                count += 1
                count_real += 1
    return count_real / count
            
def bayes_formula(n, x):
    return ((n - 1)/n * (1/6)**x) / ((n - 1)/n * (1/6)**x + 1/n)
