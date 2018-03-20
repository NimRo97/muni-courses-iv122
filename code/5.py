from SVG import Svg
from random import uniform, choice
from math import sqrt, pi, sin, cos

def random_lines(n, count, l):
    
    lines = []
    
    for i in range(count):
        
        point = (uniform(0, n), uniform(0, n))
        ang = uniform(0, 2*pi)
        point2 = (point[0] + cos(ang)*l, point[1] + sin(ang)*l)
        lines.append((point, point2))
        
    return lines


def random_points(n, count):
    points = []
    for i in range(count):
        points.append((uniform(0, n), uniform(0, n)))
    return points


def square_points(n, count):
    
    l = n/count
    points = []
    
    for i in range(count):
        for j in range(count):
            
            x = j*l + uniform(-0.1, 0.1)
            y = i*l + uniform(-0.1, 0.1)
            points.append((x, y))
            
    return points


def hexa_points(n, count):
    
    l = n/count
    h = sqrt(l**2 - (l/2)**2)
    points = []
    
    for i in range(1, count):
        for j in range(count):
            
            x = j*l + (i%2)*(l/2) + uniform(-0.1, 0.1)
            y = i*h + uniform(-0.1, 0.1)
            if (i % 2 == 0 and j % 3 != 1) or (i % 2 == 1 and j % 3 != 2):
                points.append((x, y))
                
    return points


def cross_point(line1, line2, eps=0):
    
    ((xa, ya), (xb, yb)) = line1
    ((xc, yc), (xd, yd)) = line2
    
    xp = ((xa*yb - ya*xb)*(xc - xd) - (xa - xb)*(xc*yd - yc*xd))\
         /((xa - xb)*(yc - yd) - (ya - yb)*(xc - xd))
    
    yp = ((xa*yb - ya*xb)*(yc - yd) - (ya - yb)*(xc*yd - yc*xd))\
         /((xa - xb)*(yc - yd) - (ya - yb)*(xc - xd))
    
    return xp, yp, xp > min(xa, xb)-eps and xp < max(xa, xb)+eps \
           and xp > min(xc, xd)-eps and xp < max(xc, xd)+eps


def crosses(n, count, l):
    
    im = Svg("crosses.svg")
    lines = random_lines(n, count, l)
    
    for line in lines:
        ((xa, ya), (xb, yb)) = line
        im.line(xa, ya, xb, yb)
        
    for i in range(count):
        for j in range(i + 1, count):
            (xp, yp, on_line) = cross_point(lines[i], lines[j])
            if on_line:
                im.line(xp - 1.5, yp - 1.5, xp + 1.5, yp + 1.5, "red", 4)
                
    im.close()


def triangulation_random(n, count):
    im = Svg("triang.svg")
    points = random_points(n, count)
    lines = []
    triang_lines = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            lines.append((points[i], points[j]))
    while len(lines) > 0:
        new_line = choice(lines)
        crossing = False
        for line in triang_lines:
            x, y, cross = cross_point(line, new_line, -0.001)
            if cross:
                crossing = True
        if not crossing:
            triang_lines.append(new_line)
        lines.remove(new_line)
    for line in triang_lines:
        ((xa, ya), (xb, yb)) = line
        im.line(xa, ya, xb, yb)
    im.close()


def line_length(line):
    (xa, ya), (xb, yb) = line
    return sqrt((xa-xb)**2 + (ya-yb)**2)


def triangulation_heuristic(n, count, points_f=random_points):
    
    im = Svg("triang.svg")
    points = points_f(n, count)
    lines = []
    triang_lines = []
    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            lines.append((points[i], points[j]))
    lines.sort(reverse = True, key = line_length)
    
    while len(lines) > 0:
        new_line = lines.pop()
        crossing = False
        
        for line in triang_lines:
            x, y, cross = cross_point(line, new_line, -0.00001)
            if cross:
                crossing = True
        if not crossing:
            triang_lines.append(new_line)
            
    for line in triang_lines:
        ((xa, ya), (xb, yb)) = line
        if line_length(line) > n/count + 3:
            im.line(xa, ya, xb, yb)
            
    im.close()

def convex_wrap():
    #TODO
    pass
