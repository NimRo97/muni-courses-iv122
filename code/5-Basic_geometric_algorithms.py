from SVG import Svg
from random import uniform, choice
from math import sqrt, pi, sin, cos, atan2, degrees


def random_lines(n, count, l):
    """
    Random lines (count lines) of the same length (l) spread over approximately
    square canvas of size n (can vary depending on the lines generated)
    """
    
    lines = []
    
    for i in range(count):
        
        point = (uniform(0, n), uniform(0, n))
        ang = uniform(0, 2*pi)
        point2 = (point[0] + cos(ang)*l, point[1] + sin(ang)*l)
        lines.append((point, point2))
        
    return lines


def random_points(n, count):
    """
    Generates absolutely random count points over square canvas of size n
    """
    
    points = []
    for i in range(count):
        points.append((uniform(0, n), uniform(0, n)))
    return points


def square_points(n, count):
    """
    Generates points in square grid with added random noise
    """
    
    l = n/count
    points = []
    
    for i in range(count):
        for j in range(count):
            
            x = j*l + uniform(-0.1, 0.1)
            y = i*l + uniform(-0.1, 0.1)
            points.append((x, y))
            
    return points


def hexa_points(n, count):
    """
    Generates points in hexagonal grid with added random noise
    """
    
    l = n/count
    h = sqrt(l**2 - (l/2)**2)
    points = []
    
    for i in range(1, count):
        for j in range(count):
            
            x = j*l + (i%2)*(l/2) + uniform(-0.1, 0.1)
            y = i*h + uniform(-0.1, 0.1)
            #computations needed to skip certain points
            if (i % 2 == 0 and j % 3 != 1) or (i % 2 == 1 and j % 3 != 2):
                points.append((x, y))
                
    return points


def cross_point(line1, line2, eps=0):
    """
    Computes crossing point of 2 lines and returns its coordinates plus
    True, if the point lyes on both lines (with tolerance eps), False otherwise
    """
    
    ((xa, ya), (xb, yb)) = line1
    ((xc, yc), (xd, yd)) = line2
    
    xp = ((xa*yb - ya*xb)*(xc - xd) - (xa - xb)*(xc*yd - yc*xd))\
         /((xa - xb)*(yc - yd) - (ya - yb)*(xc - xd))
    
    yp = ((xa*yb - ya*xb)*(yc - yd) - (ya - yb)*(xc*yd - yc*xd))\
         /((xa - xb)*(yc - yd) - (ya - yb)*(xc - xd))
    
    return (xp, yp,
            xp > min(xa, xb)-eps and xp < max(xa, xb)+eps \
           and xp > min(xc, xd)-eps and xp < max(xc, xd)+eps)


def crosses(n, count, l):
    """
    Genrates lines using random_lines and computes their crossing points.
    Prints lines and crossing points (in red) to .svg file
    """
    
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
    """
    Random triangulation, ugly code I won't use, just for refference, gives
    awful results
    """
    
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
    """
    Triangulation using rule shortest lines first. Bad time complexity,
    nice results.
    """
    
    im = Svg("triang.svg")
    points = points_f(n, count)
    lines = []
    triang_lines = []

    #line generation and sorting
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            lines.append((points[i], points[j]))
    lines.sort(reverse = True, key = line_length)
    
    while len(lines) > 0:
        new_line = lines.pop()
        crossing = False

        #check for crossing
        for line in triang_lines:
            x, y, cross = cross_point(line, new_line, -0.00001)
            if cross:
                crossing = True
        if not crossing:
            triang_lines.append(new_line)

    #printing        
    for line in triang_lines:
        ((xa, ya), (xb, yb)) = line
        im.line(xa, ya, xb, yb)
            
    im.close()

def angle(p1, p2, p3):
    if p1 == p2 or p2 == p3:
        return 360
    x1, y1 = p3[0] - p1[0], p3[1] - p1[1]
    x2, y2 = p2[0] - p1[0], p2[1] - p1[1]
    dot = x1*x2 + y1*y2
    det = x1*y2 - y1*x2
    return degrees(atan2(det, dot)) % 360

def convex_wrap(n, count, points_f=random_points):
    
    im = Svg("convex_wrap.svg")
    points = points_f(n, count)
    lines = []
    
    for (x, y) in points:
        im.line(x - 1.5, y - 1.5, x + 1.5, y + 1.5, "red", 4)

    start_point = min(points, key = lambda p: p[1])

    actual_point = start_point
    previous_point = (actual_point[0] - 100, actual_point[1])
    next_point = None
    while next_point != start_point:
        next_point = min(points, key = lambda p: angle(actual_point,
                                                       p, previous_point))
        lines.append((actual_point, next_point))
        previous_point = actual_point
        actual_point = next_point
    
    for line in lines:
        ((xa, ya), (xb, yb)) = line
        im.line(xa, ya, xb, yb)
            
    im.close()
