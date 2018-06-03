from SVG import Svg
from copy import deepcopy
from math import sin, cos, radians

SQUARE = [((0, 0), (500, 0)),
          ((500, 0), (500, 500)),
          ((500, 500), (0, 500)),
          ((0, 500), (0, 0))]

SQUARE_2 = [((-50, -50), (50, -50)),
            ((50, -50), (50, 50)),
            ((50, 50), (-50, 50)),
            ((-50, 50), (-50, -50))]

RECTANGLE = [((-250, 0), (250, 0)),
             ((250, 0), (250, 1000)),
             ((250, 1000), (-250, 1000)),
             ((-250, 1000), (-250, 0))]

LINE = [((0, 0), (0, 200))]

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

def operation(a, b, c, d, e, f):
    return ((a, b, e),
            (c, d, f),
            (0, 0, 1))

def test():
    im = Svg("test.svg")
    sq = deepcopy(SQUARE_2)
    for line in sq:
        im.line(line[0][0], line[0][1], line[1][0], line[1][1])
    trans = [shear(1.3), rotation(-10), scaling(0.9, 0.9),
             translation(50, 50)]
    for i in range(15):
        for i in range(4):
            p1, p2 = sq[i][0], sq[i][1]
            for tran in trans:
                p1, p2 = apply(p1, tran), apply(p2, tran)
            sq[i] = (p1, p2)
        for line in sq:
            im.line(line[0][0], line[0][1], line[1][0], line[1][1])
    im.close()
        
def mcrm(base, trans, iters):

    im = Svg("test.svg")
    for i in range(iters):
        new_base = []
        for line in base:
            for tran in trans:
                p1, p2 = line
                for t in tran:
                    p1, p2 = apply(p1, t), apply(p2, t)
                new_base.append((p1, p2))
        base = new_base

    for line in base:
        im.line(line[0][0], line[0][1], line[1][0], line[1][1])
    im.close()

#DATA--------------------------------------------------------------------------

s1_b = SQUARE
s1_t = [[scaling(0.5, 0.5)],
        [scaling(0.5, 0.5), translation(250, 0)],
        [scaling(0.5, 0.5), translation(0, 250)]]

barn_b = LINE
barn_t = [[operation(0.849, 0.037, -0.037, 0.849, 0.075*200, 0.183*200)],
          [operation(0.197, -0.226, 0.226, 0.197, 0.4*200, 0.049*200)],
          [operation(-0.15, 0.283, 0.26, 0.237, 0.575*200, 0.084*200)],
          [operation(0, 0, 0, 0.16, 0.5*200, 0)]]

star_b = SQUARE
star_t = [[operation(0.255, 0, 0, 0.255, 0.3726*500, 0.6714*500)],
          [operation(0.255, 0, 0, 0.255, 0.1146*500, 0.2232*500)],
          [operation(0.255, 0, 0, 0.255, 0.6307*500, 0.2232*500)],
          [operation(0.370, -0.642, 0.642, 0.370, 0.6356*500, -0.0061*500)]]
