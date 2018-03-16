from PIL import Image
from math import pi, sin, cos, sqrt

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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

    im.show()

def circular_implicit(r):

    im = Image.new("RGB", (2*r, 2*r), WHITE)
    for x in range(2*r):
        for y in range(2*r):
            if abs((x - r)**2 + (y - r)**2 - (r)**2) <= 50:
                im.putpixel((x, y), BLACK)

    im.show()
    
def circular_parametric(r, quality = 500):

    im = Image.new("RGB", (2*r+1, 2*r+1), WHITE)
    for deg in range(quality):
        t = (pi*2*deg)/quality
        x = round(r + cos(t) * r)
        y = round(r + sin(t) * r)
        im.putpixel((x, y), BLACK)
        
    im.show()

def spiral(r, n = 5, quality = 50):
    q = r * n * quality
    im = Image.new("RGB", (2*r+1, 2*r+1), WHITE)
    for deg in range(q):
        t = (pi*deg*n)/q % pi * 2
        x = round(r + cos(t) * r*deg/q)
        y = round(r + sin(t) * r*deg/q)
        im.putpixel((x, y), BLACK)
        
    im.show()

def triangle(n, color_f = color_f_triangle):
    h = round(sqrt(n**2 - (n/2)**2))
    im = Image.new("RGB", (n, h), WHITE)
    for x in range(n):
        for y in range(h):
            if y > 2*h/n * x - h and y > -2*h/n * x + h:
                im.putpixel((x, y), color_f(x, y, n))
                
    im.show()

def weird_ellypse(r):

    im = Image.new("RGB", (2*r, 2*r), WHITE)
    for x in range(2*r):
        for y in range(2*r):
            if ((x - r)/2)**2 + (y - r)**2 <= (r)**2:
                c = 255/r(((x - r)/2)**2 + (y - r)**2)
                im.putpixel((x, y), (c, c, c))

    im.show()
