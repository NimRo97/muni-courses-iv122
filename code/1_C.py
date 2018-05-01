from PIL import Image
from math import sqrt

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def prime(n):
    if n > 2 and n % 2 == 0: 
        return False
    return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))

def digit_sum(n):
    return sum([int(x) for x in str(n)])

def ulam(n, f):

    im = Image.new("RGB", (n, n), WHITE)

    x = n//2
    y = n//2
    step = 1
    num = 0
        
    while x >= 0 and y >= 0 and x < n and y < n:
        
        for i in range(step):
            if (f(num)) and x >= 0 and y >= 0 and x < n and y < n:
                im.putpixel((x, y), BLACK)
            x += 1
            num += 1

        for i in range(step):
            if (f(num)) and x >= 0 and y >= 0 and x < n and y < n:
                im.putpixel((x, y), BLACK)
            y -= 1
            num += 1

        step += 1

        for i in range(step):
            if (f(num)) and x >= 0 and y >= 0 and x < n and y < n:
                im.putpixel((x, y), BLACK)
            x -= 1
            num += 1
            
        for i in range(step):
            if (f(num)) and x >= 0 and y >= 0 and x < n and y < n:
                im.putpixel((x, y), BLACK)
            y += 1
            num += 1

        step += 1
    
    im.show()
    im.save("ulam.bmp")
