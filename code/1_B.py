from PIL import Image
from SVG import Svg
from math import sin, cos, radians


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def cf_black(x1, y1, x2, y2, i, line_count):
    return BLACK
    
def test_picture(n):

    im = Image.new("RGB", (n, n), (255, 255, 255))

    for i in range(n):
        for j in range(n):
            im.putpixel((i, j), (256 * i // n, 0, 256 * j // n))
    im.show()

def star_quadrant(im, length, start, end, line_count, color_f):

    x1, y1, x2, y2 = start
    for i in range(line_count):
        r, g, b = color_f(x1, y1, x2, y2, i, line_count)
        rgb = "rgb(" + str(r) + ", " + str(g) + ", " + str(b) + ")"
        im.line(x1, y1, x2, y2, rgb)
        x1 += (end[0] - start[0]) / line_count
        y1 += (end[1] - start[1]) / line_count
        x2 += (end[2] - start[2]) / line_count
        y2 += (end[3] - start[3]) / line_count

def star(length, n, line_count, color_f=cf_black):

    im = Svg("star.svg")
    for i in range(n):
        x2 = cos(radians(360 / n * i)) * length
        y2 = sin(radians(360 / n * i)) * length
        x1 = cos(radians(360 / n * (i + 1))) * length
        y1 = sin(radians(360 / n * (i + 1))) * length
        star_quadrant(im, 0, (0, 0, x2, y2), (x1, y1, 0, 0),
                      line_count, color_f)
    im.close()
