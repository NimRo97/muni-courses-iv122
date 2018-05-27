from PIL import Image
from math import pi, sin, cos, radians

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def e1(n, l, r):

    im = Image.new("RGB", (n * l, n * l), WHITE)
    
    for x in range(n * l):
        for y in range(n * l):
            t = 0
            if x // l % 2 == 1:
                t += 1
            if y // l % 2 == 1:
                t += 1
            if round((abs(x - n*l/2)**2 + abs(y - n*l/2)**2)**0.5) // r % 2 == 1:
                t += 1
            if t % 2 == 1:
                c = BLACK
            else:
                c = WHITE
            im.putpixel((x, y), c)

    im.save("e1_"+str(n)+"_"+str(l)+"_"+str(r)+".png", "PNG")

def e2(n, n2):

    im = Image.new("RGB", (n, n), WHITE)
    
    for x in range(n):
        for y in range(n):
            c = round(255*(cos(radians(((x-n/2)**2+(y-n/2)**2)**0.5)*10)+1)/2)
            if x >= (n - n2)/2 and y >= (n - n2)/2 and \
               x < (n + n2)/2 and y < (n + n2)/2:
                im.putpixel((x, y), (255-c, 255-c, 255-c))
            else:
                im.putpixel((x, y), (c, c, c))

    im.save("e2_"+str(n)+"_"+str(n2)+".png", "PNG")

def e3(n):

    im = Image.new("RGB", (n, n), WHITE)
    
    for x in range(n):
        for y in range(n):
            r = round(255*(sin(radians(x)*7)+1)/2)
            g = round(255*(sin(radians(x + y)*7)+1)/2)
            b = round(255*(sin(radians(y)*7)+1)/2)
            im.putpixel((x, y), (r, g, b))
            
    im.save("e3_"+str(n)+".png", "PNG")

def m1(n, d):

    im = Image.new("RGB", (n, n), WHITE)
    
    for x in range(n):
        for y in range(n):
            r = round(255*(sin(radians(x - y)*7)+1)/2)
            g = round(255*(cos(radians(x + y)*7)+1)/2)
            b = round(255*(cos(radians(x + y)*7)+1)/2)
            if (abs(x - n/2)**2 + abs(y - n/2)**2)**0.5 // d % 2 == 1:
                im.putpixel((x, y), (r, g, b))
            else:
                im.putpixel((x, y), (r, 255-g, 255-b))
            
    im.save("m1_"+str(n)+"_"+str(d)+".png", "PNG")

def m2(n):

    im = Image.new("RGB", (n, n), WHITE)
    
    for x in range(n):
        for y in range(n):
            r = round(255*x/n)
            g = round(255-255*x/n)
            b = round(255*(sin(radians(y)*7)+1)/2)
            im.putpixel((x, y), (r, g, b))
            
    im.save("m2_"+str(n)+".png", "PNG")
