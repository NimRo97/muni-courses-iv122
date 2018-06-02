from PIL import Image
from math import sin, cos, radians, sqrt
from random import choice
#chaos_game(2000, 4, 1/3, 1000000)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
def black(a, b, c):
    return BLACK
def white(a, b, c):
    return WHITE

def color_f_nice(x, y, n):
    h = round(sqrt(n**2 - (n/2)**2))
    b = round(255/h*y)
    r = round(255/n*sqrt(x**2+(h-y)**2))
    g = round(255/n*sqrt((n-x)**2+(h-y)**2))
    return r, g, b

def chaos_game(size, n, r, count, color_f = black):

    radius = 0.48*size
    middle = size / 2
    
    im = Image.new("RGB", (size, size), BLACK)
    points = []

    for i in range(n):
        x = middle + cos(radians(360 / n * i)) * radius
        y = middle + sin(radians(360 / n * i)) * radius
        points.append((x, y))

    x, y = points[0]

    for i in range(count):
         rx, ry = choice(points)
         x = x + (1 - r)*(rx - x)
         y = y + (1 - r)*(ry - y)
         im.putpixel((round(x), round(y)), color_f(x, y, radius))

    im.save("chaos.png", "PNG")
