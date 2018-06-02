from PIL import Image

COLOR = (128, 64, 192)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

"""
    size - vertical resolution with maximum x range
    r1, r2 - range of r, 0 - 4
    x1, x2 - range of x, 0 - 1
"""
def feinberg(size, detail=10000, r1 = 0, r2 = 4, x1 = 0, x2 = 1):
    
    im = Image.new("RGB",
                   (round(size * (r2 - r1)), round(size * (x2 - x1))),
                   WHITE)

    for r in [x * (1 / detail) for x in range(1, detail)]:
        x = 0.1
        for i in range(200):
            x = 4 * r * x * (1 - x)
            if i >= 100 and r > r1 / 4 and r < r2 / 4 and x > x1 and x < x2:
                im.putpixel((round((r - r1 / 4) * (size - 1) * 4),
                             round((1 - x - x1) * (size - 1))), COLOR)

    im.save("feinberg.png", "PNG")

