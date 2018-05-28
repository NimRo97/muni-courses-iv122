from PIL import Image
from math import pi, sin, cos, sqrt, radians

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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

def rotation(a):
    a = radians(a)
    return ((cos(a), -sin(a), 0),
            (sin(a),  cos(a), 0),
            (0,       0,      1))

def color_f_triangle(x, y, n):
    h = round(sqrt(n**2 - (n/2)**2))
    b = round(255/h*y)
    r = round(255/n*sqrt(x**2+(h-y)**2))
    g = round(255/n*sqrt((n-x)**2+(h-y)**2))
    return r, g, b

    
def circle(r):

    im = Image.new("RGB", (2*r, 2*r), WHITE)
    for x in range(2*r):
        for y in range(2*r):
            if (x - r)**2 + (y - r)**2 <= (r)**2:
                im.putpixel((x, y), BLACK)

    im.save("circle_"+str(r)+".png", "PNG")

def circular_implicit(r):

    im = Image.new("RGB", (2*r, 2*r), WHITE)
    for x in range(2*r):
        for y in range(2*r):
            if abs((x - r)**2 + (y - r)**2 - (r)**2) <= 50:
                im.putpixel((x, y), BLACK)

    im.save("circular_implicit_"+str(r)+".png", "PNG")
    
def circular_parametric(r, quality = 500):

    im = Image.new("RGB", (2*r+1, 2*r+1), WHITE)
    for deg in range(quality):
        t = (pi*2*deg)/quality
        x = round(r + cos(t) * r)
        y = round(r + sin(t) * r)
        im.putpixel((x, y), BLACK)
        
    im.save("circular_param_"+str(r)+"_"+str(quality)+".png", "PNG")

def spiral(r, n = 5, quality = 50):
    q = r * n * quality
    im = Image.new("RGB", (2*r+1, 2*r+1), WHITE)
    for deg in range(q):
        t = (pi*deg*n)/q % pi * 2
        x = round(r + cos(t) * r*deg/q)
        y = round(r + sin(t) * r*deg/q)
        c = (round(abs(sin(t)) * 255), round(max(0, -cos(t)) * 255),
             round(max(0, cos(t)) * 255))
        im.putpixel((x, y), c)
        
    im.save("spiral_"+str(r)+"_"+str(n)+"_"+str(quality)+".png", "PNG")

def triangle(n, color_f = color_f_triangle):
    h = round(sqrt(n**2 - (n/2)**2))
    im = Image.new("RGB", (n, h), WHITE)
    for x in range(n):
        for y in range(h):
            if y > 2*h/n * x - h and y > -2*h/n * x + h:
                im.putpixel((x, y), color_f(x, y, n))
                
    im.save("triangle_"+str(n)+".png", "PNG")

def ellipse_rotated(r, a=1, b=1, psi=0):

    im = Image.new("RGB", (2*r, 2*r), WHITE)
    for x in range(2*r):
        for y in range(2*r):
            xi, yi = apply((x - r, -(y - r)), rotation(-psi))
            xi, yi = round(xi + r), round(-yi + r)
            if ((xi - r)*a)**2 + ((yi - r)*b)**2 <= (r)**2:
                c = round(255*(((xi - r)*a)**2 + ((yi - r)*b)**2)/((r)**2))
                im.putpixel((x, y), (c,c,c))

    im.save("ellipse_"+str(r)+"_"+str(a)+"_"+str(b)+"_"+str(psi)+".png", "PNG")
