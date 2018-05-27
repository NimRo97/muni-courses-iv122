from PIL import Image
from random import randint

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def skryvacka1():

    old = Image.open("skryvacka1.png").convert("RGB")
    w, h = old.size
    im = Image.new("RGB", (w, h), WHITE)
    for x in range(w):
        for y in range(h):
            r, g, b = old.getpixel((x, y))
            if b > 0:
                b = 255
            b = 255 - b
            im.putpixel((x, y), (b, b, b))

    old.close()
    im.save("sk1.png", "PNG")

def skryvacka2():

    old = Image.open("skryvacka2.png").convert("RGB")
    w, h = old.size
    im = Image.new("RGB", (w, h), WHITE)
    for x in range(1, w):
        for y in range(1, h):
            r, g, b = old.getpixel((x, y))
            p = (r+g+b)//3
            im.putpixel((x,y),(p,p,p))

    old.close()
    im.save("sk2.png", "PNG")

def myCipher(text):
    im = Image.new("RGB", (len(text), len(text)), WHITE)
    for x in range(len(text)):
        for y in range(len(text)):
            r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
            if x == y:
                b = ord(text[x])
            im.putpixel((x, y), (r, g, b))
    im.save("cipher.png", "PNG")

def myDecipher():
    s = ""
    im = Image.open("cipher.png").convert("RGB")
    for i in range(im.size[0]):
        s += chr(im.getpixel((i, i))[2])
    print(s)
        
