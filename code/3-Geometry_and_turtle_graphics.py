from turtle import Turtle
from MyTurtle import MyTurtle
from SVG import Svg
from math import sqrt, sin, cos, acos, atan, radians, degrees
julie = MyTurtle()
julie.speed(10000)

def poly(n, l):
    for i in range(n):
        julie.forward(l)
        julie.right(360/n)

def diamond(n, l):
    for i in range(n):
        poly(n, l)
        julie.right(360/n)

def square(l):
    poly(4, l)

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


def pentagram_turtle(l):
    li = l * cos(radians(36)) * 2
    for i in range(5):
        julie.forward(l)
        julie.left(72)
    julie.left(36)
    for i in range(5):
        julie.forward(li)
        julie.left(144)

def pentagram_absolute(l):
    im = Svg("penta_" + str(l) + ".svg")
    points = []
    for i in range(5):
        points.append((cos(radians(72 * i)) * l, sin(radians(72 * i)) * l))
    for i in range(5):
        im.line(points[i][0], points[i][1],
                points[(i + 1) % 5][0], points[(i + 1) % 5][1])
        im.line(points[i][0], points[i][1],
                points[(i + 2) % 5][0], points[(i + 2) % 5][1])
    im.close()

def circle_lines(r, count):
    im = Svg("circle_lies_" + str(r) + "_" + str(count) + ".svg")
    for i in range(count):
        x = -r + r * 2 / count * i
        y = sin(acos(x / r)) * r
        im.line(x, y, x, -y)
        im.line(y, x, -y, x)
    im.close()

def nested_polygons(poly=3, size=200, count=10):
    
    im = Svg("poly.svg")
    points = []
    
    for i in range(count):
        r = size / count * (i + 1)
        points = []
        for j in range(poly):
            points.append((cos(radians(360 / poly * j)) * r,
                           sin(radians(360 / poly * j)) * r))
        for i in range(poly):
            im.line(points[i][0], points[i][1],
                    points[(i + 1) % poly][0], points[(i + 1) % poly][1])
            
    im.close()
    
def tree(l):
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

def krishna(depth, length):
    julie.pu()
    julie.forward(length/2)
    julie.left(135)
    for i in range(4):
        julie.pd()
        julie.forward(sqrt(2)/2*length)
        if depth > 0:
            julie.right(45)
            julie.forward(length)
            julie.pu()
            julie.forward((2**depth - 1.5)*length)
            krishna(depth - 1, length)
            julie.pu()
            julie.backward((2**depth - 1.5)*length)
            julie.backward(length)
            julie.left(45)
        julie.left(90)
    julie.right(135)
    julie.pu()
    julie.backward(length/2)
            
        
