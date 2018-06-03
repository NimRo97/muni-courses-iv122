from random import randint, choice

def monty_hall(n, mode):
    right = 0
    for i in range(n):
        a = [1, 2, 3]
        win = randint(1, 3)
        guess = randint(1, 3)
        a.remove(win)
        if guess in a:
            a.remove(guess)
        show = choice(a)
        if mode == "s":       #for better readibility
            pass
        elif mode == "c":
            guess = 6 - show - guess
        elif mode == "r":
            if randint(0, 1) == 0:
                guess = 6 - show - guess
        if guess == win:
            right += 1
    print(str(right/n*100) + "%")
        

def analyse():
    for i in range(1, 8):
        res = [0]*6
        res2 = [[0]*6 for i in range(6)]
        f = open("random"+str(i)+".txt", "r")
        numbers = list(map(lambda x: int(x), f.readline().split(" ")))
        for n in numbers:
            res[n-1] += 1
        prev = numbers[0]
        for n in numbers[1:]:
            res2[prev-1][n-1] += 1
            prev = n
        print("file: random "+str(i))
        for i in range(6):
            print(i+1,":",res[i])
        for i in range(6):
            for j in range(6):
                print('{:>4}'.format(res2[i][j]), end=" ")
            print()
        print()

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
