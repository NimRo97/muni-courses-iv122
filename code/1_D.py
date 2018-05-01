from PIL import Image

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def gcd_mod(a, b, depth=0):
    if b == 0:
        return a, depth
    return gcd_mod(b, a % b, depth + 1)

def gcd_minus(a, b, depth=0):
    if a == b:
        return a, depth
    return gcd_minus(abs(a - b), min(a, b), depth + 1)

def greatest(n):

    im = Image.new("RGB", (n, n), WHITE)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            s = round(255 / n * gcd_mod(i, j)[0])
            im.putpixel((i - 1, n - j), (s, s, s))

    im.show()
    im.save("greatest.bmp")

def steps(n, f):

    im = Image.new("RGB", (n, n), WHITE)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            s = min(round(255 / 12 * f(i, j)[1]), 255)
            im.putpixel((i - 1, n - j), (s, 255-s, 63))

    im.show()
    im.save("steps.bmp")

def difference(n):

    im = Image.new("RGB", (n, n), WHITE)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            s = round(255 / (gcd_minus(i, j)[1] + 1) * (gcd_mod(i, j)[1] + 1))
            im.putpixel((i - 1, n - j), (s, s, s))

    im.show()
    im.save("diff.bmp")
