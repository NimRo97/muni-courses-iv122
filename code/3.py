from turtle import Turtle
from MyTurtle import MyTurtle
from math import sqrt, sin, atan, radians, degrees
julie = MyTurtle()
julie.speed(10000)

def square(n):
    for i in range(4):
        julie.forward(n)
        julie.right(90)

def square_spiral(n, size):
    a = size
    for i in range(n):
        square(a)
        julie.forward(a*0.25)
        julie.right(90-degrees(atan(3)))
        a = sqrt((a/4)**2 + (0.75*a)**2)

def nested_squares(depth, l=180.0):
    for i in range(4):
        julie.forward(l)
        julie.right(90)
    if depth>1:
        julie.forward(l/2)
        julie.right(45)
        nested_squares(depth-1,((l/2)**2*2)**0.5)

def tree(l):
    julie.left(90)
    if l>5:
        julie.forward(l)
        julie.left(45)
        tree(l*0.6)
        julie.right(90)
        tree(l*0.6)
        julie.left(45)
        julie.backward(l)

def fractal(s): #lines only
    if s>5:
        for i in range(3):
            fractal(s/2)
            julie.forward(s)
            julie.left(120)

def fractal2(s): #black "background"
    if s>10:
        julie.begin_fill()
        for i in range(3):
            fractal2(s/2)
            julie.forward(s)
            julie.left(120)
        julie.end_fill()

def koch(l):
    if l<10:
        julie.forward(l)
    else:
        koch(l/3)
        julie.left(60)
        koch(l/3)
        julie.right(120)
        koch(l/3)
        julie.left(60)
        koch(l/3)

def snowflake(l):
    for i in range(3):
        koch(l)
        julie.right(120)

def koch2(l,p):
    if l<5:
        julie.forward(l)
    else:
        julie.left(p*30)
        koch2(l/1.7,p*-1)
        julie.right(p*60)
        koch2(l/1.7,p*-1)
        julie.left(p*30)

def snowflake2(l):
    for i in range(3):
        koch2(l,1)
        julie.right(120)

def cookie(l):
    julie.pu()
    julie.forward(l/3)
    julie.right(90)
    julie.forward(l/3)
    julie.pd()
    julie.begin_fill()
    for i in range(4):
        julie.forward(l/3)
        julie.left(90)
    julie.end_fill()
    julie.pu()
    julie.backward(l/3)
    julie.left(90)
    julie.backward(l/3)
    if l>30:
        julie.forward(l/3)
        for j in range(4):
            for i in range(2):
                cookie(l/3)
                julie.forward(l/3)
            julie.right(90)
            julie.forward(l/3)
        julie.backward(l/3)

def hilbert(depth=5, d=1, l=10):
    if depth == 1:
        julie.forward(l)
        julie.right(d*90)
        julie.forward(l)
        julie.right(d*90)
        julie.forward(l)
    else:
        julie.right(d*90)
        hilbert(depth-1,-d,l)
        julie.right(d*90)
        julie.forward(l)
        hilbert(depth-1,d,l)
        julie.left(d*90)
        julie.forward(l)
        julie.left(d*90)
        hilbert(depth-1,d,l)
        julie.forward(l)
        julie.right(d*90)
        hilbert(depth-1,-d,l)
        julie.right(d*90)

def penta_star(l):
    julie.pu()
    ln = l / (2 * (1 + sin(radians(18))))
    for i in range(5):
        if l > 20:
            penta_star(ln)
        else:
            julie.pd()
        julie.forward(l)
        julie.pu()
        julie.right(72)
    julie.forward(ln)
    julie.right(72)
    julie.forward(ln)
    julie.left(36)
    if l > 20:
        penta_star(ln)
    julie.right(36)
    julie.backward(ln)
    julie.left(72)
    julie.backward(ln)
