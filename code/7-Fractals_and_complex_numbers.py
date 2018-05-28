from PIL import Image
from multiprocessing import Pool
from functools import partial
from datetime import datetime
from math import sqrt

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def mandelbrot_point(d, res, iter_count, x1, x2, y1, y2):

    x, y = d
    c = complex(x, y)
    z = 0 + 0j
    vals = []
    steps = 0
    abs2 = 0
    while abs2 <= 4 and steps < iter_count:
        z = pow(z, 2) + c
        abs2 = z.real**2 + z.imag**2
        vals.append(abs2)
        steps += 1
        
    if abs2 <= 4:
        
        if (x, y) == (0, 0):
            avg = 255
        else:
            avg = round(sum(vals)/len(vals)*255/(max(vals)))
        color = ((255-avg)//2, 0, 255-avg)

    else:
        col = round(255/iter_count*steps)
        color = (col, col, 0)

    return x, y, color

def julius_point(d, c, res, iter_count, x1, x2, y1, y2):

    x, y = d
    z = complex(x, y)
    vals = []
    steps = 0
    abs2 = 0
    while abs2 <= 4 and steps < iter_count:
        z = pow(z, 2) + c
        abs2 = z.real**2 + z.imag**2
        vals.append(abs2)
        steps += 1
        
    if abs2 <= 4:
        
        if (x, y) == (0, 0):
            avg = 255
        else:
            avg = round(sum(vals)/len(vals)*255/(max(vals)))
        color = ((255-avg)//2, 0, 255-avg)

    else:
        col = round(255/30*steps)
        color = (col, col, 0)

    return x, y, color
        

def mandelbrot(im_name="mand.png", res=100, iter_count=30,
               x1=-2, x2=1, y1=-1, y2=1):
    
    y1, y2 = -y2, -y1
    im = Image.new("RGB", (round(res*(x2-x1)), round(res*(y2-y1))), WHITE)
                   
    pixels = im.load()
                   
    doubles = [(x, y)
               for x in
               [n / res for n in range(round(x1*res), round(x2*res))]
               for y in
               [n / res for n in range(round(y1*res), round(y2*res))]]
    
    for (x, y, color) in Pool(4).map(partial(mandelbrot_point, res=res,
                                             iter_count=iter_count,
                                             x1=x1, x2=x2, y1=y1, y2=y2),
                                     doubles):
        pixels[round((x - x1) * res),
               round((y - y1) * res)] = color
        
    im.save(im_name, "PNG")

def julius(c, res=400, iter_count=30, x1=-1.5, x2=1.5, y1=-1, y2=1):

    y1, y2 = -y2, -y1

    im = Image.new("RGB", (round(res*(x2-x1)), round(res*(y2-y1))), WHITE)
                   
    pixels = im.load()
                   
    doubles = [(x, y)
               for x in
               [1/res * n for n in range(round(x1*res), round(x2*res))]
               for y in
               [1/res * n for n in range(round(y1*res), round(y2*res))]]
    
    for (x, y, color) in Pool(4).map(partial(julius_point, c=c, res=res,
                                             iter_count=iter_count,
                                             x1=x1, x2=x2, y1=y1, y2=y2),
                                     doubles):
        pixels[round(x * res - x1*res),
               round(y * res - y1*res)] = color
    
    im.save("julius.bmp", "BMP")

def mandelbrot_zoom(x1, x2, y1, y2, fx1, fx2, fy1, fy2):
    fact = 150
    reso = 600
    for factor in range(120):
        if factor % 10 == 0:
            print(factor)
        nx1 = x1 + (fx1 - x1)/fact*factor
        nx2 = x2 + (fx2 - x2)/fact*factor
        ny1 = y1 + (fy1 - y1)/fact*factor
        ny2 = y2 + (fy2 - y2)/fact*factor
        res = reso/(nx2-nx1)
        mandelbrot("mand_"+str(factor)+".png", res, 100, nx1, nx2, ny1, ny2)

def newton_point(d, res, iter_count, x1, x2, y1, y2):

    x, y = d
    if x == 0 and y == 0:
        return BLACK
    
    z = complex(x, y)
    for i in range(iter_count):
        z = z - (pow(z, 3) - 1) / (3 * pow(z, 2))
        
    r = [1, -0.5 + sqrt(3)/2j, -0.5 - sqrt(3)/2j]
    re = [abs(c - z) for c in r]
    m = max(re)

    r = round(255 * re[0] / m)
    g = round(255 * re[1] / m)
    b = round(255 * re[2] / m)

    return x, y, (r, g, b)

def newton(im_name="newton.bmp", res=100, iter_count=20,
               x1=-5, x2=5, y1=-4, y2=4):
    
    y1, y2 = -y2, -y1

    im = Image.new("RGB", (round(res*(x2-x1)), round(res*(y2-y1))), WHITE)
                   
    pixels = im.load()
                   
    doubles = [(x, y)
               for x in
               [1/res * n for n in range(round(x1*res), round(x2*res))]
               for y in
               [1/res * n for n in range(round(y1*res), round(y2*res))]]
    
    for (x, y, color) in Pool(4).map(partial(newton_point, res=res,
                                             iter_count=iter_count,
                                             x1=x1, x2=x2, y1=y1, y2=y2),
                                     doubles):
        pixels[round(x * res - x1*res),
               round(y * res - y1*res)] = color
    
    im.save(im_name, "BMP")
