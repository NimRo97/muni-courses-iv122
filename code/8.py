from SVG import Svg
from copy import deepcopy
from math import sin, cos, radians

SQUARE = [((0, 0), (50, 0)),
          ((50, 0), (50, 50)),
          ((50, 50), (0, 50)),
          ((0, 50), (0, 0))]

SQUARE_2 = [((-50, -50), (50, -50)),
            ((50, -50), (50, 50)),
            ((50, 50), (50, -50)),
            ((50, -50), (-50, -50))]

def multiply_row(a, b):
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

def apply(point, trans):
    point = (point[0], point[1], 1)
    x = multiply_row(trans[0], point)
    y = multiply_row(trans[1], point)
    return x, y

def translation(x, y):
    return ((1, 0, x),
            (0, 1, y),
            (0, 0, 1))

def scaling(sx, sy):
    return ((sx, 0,  0),
            (0,  sy, 0),
            (0,  0,  1))

def rotation(a):
    a = radians(a)
    return ((cos(a), -sin(a), 0),
            (sin(a),  cos(a), 0),
            (0,       0,      1))

def shear(k):
    return ((1, k, 0),
            (0, 1, 0),
            (0, 0, 1))

def test():
    im = Svg("test.svg")
    sq = deepcopy(SQUARE_2)
    for line in sq:
        im.line(line[0][0], line[0][1], line[1][0], line[1][1])
    trans = [rotation(-10), scaling(1.1, 0.8)]
    for i in range(15):
        for i in range(4):
            p1, p2 = sq[i][0], sq[i][1]
            for tran in trans:
                p1, p2 = apply(p1, tran), apply(p2, tran)
            sq[i] = (p1, p2)
        for line in sq:
            im.line(line[0][0], line[0][1], line[1][0], line[1][1])
    im.close()
        
