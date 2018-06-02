from MyTurtle import MyTurtle
from random import randint

class Stochastic():

    def __init__(self, options):
        self.options = options
        self.count = sum(val for option, val in options)

    def option(self):
        r = randint(1, self.count)
        i = 0
        for option in self.options:
            i += option[1]
            if i >= r:
                return option[0]

class LSystem():

    def __init__(self, name, axiom, rules, draw_rules):
        self.name = name
        self.axiom = axiom
        self.rules = rules
        self.draw_rules = draw_rules

    def rule(self, r):
        if isinstance(self.rules[r], str):
            return self.rules[r]
        else:
            return self.rules[r].option()

def black_c(n, max_n):
    return "black", 1

def l_system(system, iterations, f=5, color_f=black_c, turtle=None):

    old = system.axiom
    n = 0
    max_n = 0
    
    for i in range(iterations):
        
        new = ""
        for c in old:
            if c in system.rules.keys():
                new += system.rule(c)
            else:
                new += c
                if c == "[":
                    n += 1
                if c == "]":
                    n -= 1
                if n > max_n:
                        max_n = n
        old = new

    name = system.name
    julie = turtle
    if turtle is None:
        julie = MyTurtle(name)
        julie.heading = 90
    
    n = 0
    julie.color, julie.stroke = color_f(n, iterations)
    status = []
    for c in new:
        if c == "+":
            julie.right(system.draw_rules["r"])
        elif c == "-":
            julie.left(system.draw_rules["l"])
        elif c in system.draw_rules["f"]:
            julie.forward(f)
        elif c == "[":
            n += 1
            julie.color, julie.stroke = color_f(n, max_n)
            status.append((julie.x, julie.y, julie.heading))
        elif c == "]":
            n -= 1
            julie.color, julie.stroke = color_f(n, max_n)
            julie.x, julie.y, julie.heading = status.pop()

    if turtle is None:
        julie.save()


#DATA--------------------------------------------------------------------------

koch = LSystem("koch",
               "F--F--F",
               {"F" : "F+F--F+F"},
               {"r" : 60,
                "l" : 60,
                "f" : "F"})

sierpinski = LSystem("sierpinski",
                     "A",
                     {"A" : "B-A-B",
                      "B" : "A+B+A"},
                     {"r" : 60,
                      "l" : 60,
                      "f" : "AB"})

hilbert = LSystem("hilbert",
                  "A",
                  {"A" : "-BF+AFA+FB-",
                   "B" : "+AF-BFB-FA+"},
                  {"r" : 90,
                   "l" : 90,
                   "f" : "F"})

tree = LSystem("tree",
               "A",
               {"A" : "F[+A]-A",
                "F" : "FF"},
               {"r" : 45,
                "l" : 45,
                "f" : "F"})

tree2 = LSystem("tree2",
                "A",
                {"A" : "F-[[A]+A]+F[+FA]-A",
                 "F" : "FF"},
                {"r" : 25,
                 "l" : 25,
                 "f" : "F"})

tree3 = LSystem("tree3",
                "F",
                {"F" : "FF+[+F-FF]-[-F+F+F]"},
                {"r" : 25,
                 "l" : 25,
                 "f" : "F"})

stoch_tree = LSystem("stochastic_tree",
                     "F",
                     {"F" : Stochastic([("F[+F]F[-F]F", 1),
                                        ("F[+F]F", 1),
                                        ("F[-F]F", 1)])},
                     {"r" : 30,
                      "l" : 30,
                      "f" : "F"})

#COLORS------------------------------------------------------------------------

def tree_c(n, max_n):
    g = round(192 * n / max_n)
    r = 64
    if n >= max_n - 2 and randint(1, 3) == 1:
        r == 255
        g = 192
        c = randint(1, 3)
        if c == 1:
            g = 255
        if c == 2:
            g = 128
    return "rgb("+str(r)+","+str(g)+",0)", 2 - 1 * n / max_n

def grass_c(n, max_n):
    g = 127 + round(128 * n / max_n)
    return "rgb(0,"+str(g)+",0)", 0.8

#ADVANCED----------------------------------------------------------------------

def forest(n):

    julie = MyTurtle("forest")

    for i in range(n):
        julie.heading = 90
        julie.y = 0
        julie.x = i*3
        r = randint(1,30)
        if r <= 10:
            l_system(tree2, randint(2, 4), 1, grass_c, julie)
        elif r == 16:
            l_system(tree3, randint(2, 5), randint(5, 7), tree_c, julie)
        elif r == 17 or r == 18:
            l_system(tree3, randint(2, 4), randint(2, 9), tree_c, julie)
        else:
            l_system(stoch_tree, randint(2, 4), 1, grass_c, julie)

    julie.save()
