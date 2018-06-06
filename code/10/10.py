def readpoints(file):
    f = open(file, "r")
    points = []
    for line in f.readlines():
        l = line.rstrip().split(" ")
        x = l[0]
        y = l[1]
        points.append((float(x), float(y)))
    return points

def linreg(points):
    sx, sy, sx2, sxy = 0, 0, 0, 0
    for x, y in points:
        sx += x
        sy += y
        sx2 += x ** 2
        sxy += x * y
    print(sxy, sx2, sx, sy)
    a = (len(points) * sxy - sx  * sy) /\
        (len(points) * sx2 - sx ** 2)
    b = (sy - a * sx) / len(points)

    return a, b
