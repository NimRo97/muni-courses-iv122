from PIL import Image

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def change(c):
    return BLACK if c == WHITE else WHITE

def cross_point(line1, line2, eps=0):
    
    ((xa, ya), (xb, yb)) = line1
    ((xc, yc), (xd, yd)) = line2
    
    xp = ((xa*yb - ya*xb)*(xc - xd) - (xa - xb)*(xc*yd - yc*xd))\
         /((xa - xb)*(yc - yd) - (ya - yb)*(xc - xd))
    
    yp = ((xa*yb - ya*xb)*(yc - yd) - (ya - yb)*(xc*yd - yc*xd))\
         /((xa - xb)*(yc - yd) - (ya - yb)*(xc - xd))

    on_line = xp > min(xa, xb)-eps and xp < max(xa, xb)+eps \
              and xp > min(xc, xd)-eps and xp < max(xc, xd)+eps
    
    return (xp, yp, on_line)

def polygon(poly):

    width = max([p[0] for p in poly]) + 1
    height = max([p[1] for p in poly]) + 1
    n = len(poly)

    matrix = [[False] * height for i in range(width)]
    lines = [(poly[i % n], poly[(i + 1) % n]) for i in range(n)]
    
    for i in range(height):
        line = ((0, i), (width - 1, i))
        for l in lines:
            x, y, on_line = cross_point(line, l)
            if on_line:
                matrix[round(x)][round(y)] = not matrix[round(x)][round(y)]

    im = Image.new("RGB", (width, height), WHITE)
    
    
    for y in range(height):
        c = WHITE
        for x in range(width):

            if matrix[x][y]:
                c = change(c)
            im.putpixel((x, height - y - 1), c)

    im.save("polygon.png", "PNG")
