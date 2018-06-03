from random import shuffle
from SVG import Svg
from math import sqrt

class Point():

    def __init__(self, points = []):
        self.points = []
        self.ways = []
        for p in points:
            slef.points.append(p)

    def add_points(self, points):
        for p in points:
            self.points.append(p)

    def add_point(self, point):
        self.points.append(point)

    def add_ways(self, ways):
        for w in ways:
            self.wayts.append(w)

    def add_way(self, way):
        self.ways.append(way)

def generate_square(n):
    matrix = [[Point() for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if i + x >= 0 and i + x < n and j + y >=0 and j + y < n:
                    matrix[i][j].add_point(matrix[i + x][j + y])
    return matrix

def generate_hexa(n):
    
    matrix = [[Point() for x in range(n)] for y in range(n)]
    
    for i in range(n):
        for j in range(n):
            
            if j % 2 == 0:
                neighbors = [(1, 0), (-1, 0), (0, 1),
                              (0, -1), (1, 1), (1, -1)]
            else:
                neighbors = [(1, 0), (-1, 0), (0, 1),
                             (0, -1), (-1, 1), (-1, -1)]
                
            for x, y in neighbors:
                if i + x >= 0 and i + x < n and j + y >=0 and j + y < n:
                    matrix[i][j].add_point(matrix[i + x][j + y])
                    
    return matrix

def print_square(matrix, n):

    im = Svg("labirinth.svg")
    LEN = 20

    im.line(0, 0, LEN * n, 0)
    im.line(0, 0, 0, LEN * n)
    im.line(LEN * n, 0, LEN * n, LEN * n)
    im.line(0, LEN * n, LEN * n, LEN * n)
    for i in range(n):
        for j in range(n):
            
            if i < n - 1:
                if matrix[i + 1][j] not in matrix[i][j].ways:
                    im.line(LEN*(i+1), LEN*j, LEN*(i+1), LEN*(j+1))

            if j < n - 1:
                if matrix[i][j + 1] not in matrix[i][j].ways:
                    im.line(LEN*i, LEN*(j+1), LEN*(i+1), LEN*(j+1))

    im.close()

def print_hexa(matrix, n):
    
    im = Svg("labirinth.svg")
    L = 20
    D = sqrt(L ** 2 - (L / 2) ** 2)

    for i in range(n):
        for j in range(n):
            midx, midy = i * D * 2, j * 1.5 * L
            if j % 2 == 1:
                midx -= D
            
            if j == 0:
                print_side(midx, midy, L, D, 0, im)
                print_side(midx, midy, L, D, 5, im)

            if j == n - 1:
                print_side(midx, midy, L, D, 2, im)
                print_side(midx, midy, L, D, 3, im)

            if i == 0:
                if j % 2 == 0:
                    print_side(midx, midy, L, D, 4, im)
                else:
                    print_side(midx, midy, L, D, 3, im)
                    print_side(midx, midy, L, D, 4, im)
                    print_side(midx, midy, L, D, 5, im)

            if i == n-1:
                if j % 2 == 1:
                    print_side(midx, midy, L, D, 1, im)
                else:
                    print_side(midx, midy, L, D, 0, im)
                    print_side(midx, midy, L, D, 1, im)
                    print_side(midx, midy, L, D, 2, im)

            if i < n - 1:
                if matrix[i + 1][j] not in matrix[i][j].ways:
                    print_side(midx, midy, L, D, 1, im)

            if j < n - 1:
                if j % 2 == 0:
                    if matrix[i][j + 1] not in matrix[i][j].ways:
                        print_side(midx, midy, L, D, 3, im)
                    if i+1<n and matrix[i + 1][j + 1] not in matrix[i][j].ways:
                        print_side(midx, midy, L, D, 2, im)
                else:
                    if matrix[i][j + 1] not in matrix[i][j].ways:
                        print_side(midx, midy, L, D, 2, im)
                    if matrix[i - 1][j + 1] not in matrix[i][j].ways:
                        print_side(midx, midy, L, D, 3, im)

    im.close()
                
def print_side(x, y, l, d, side, im):
    if side == 0:
        x1, y1, x2, y2 = x, y - l, x + d, y - l / 2
    elif side == 1:
        x1, y1, x2, y2 = x + d, y - l / 2, x + d, y + l / 2
    elif side == 2:
        x1, y1, x2, y2 = x + d, y + l / 2, x, y + l
    elif side == 3:
        x1, y1, x2, y2 = x, y + l, x - d, y + l / 2
    elif side == 4:
        x1, y1, x2, y2 = x - d, y + l / 2, x - d, y - l / 2
    else:
        x1, y1, x2, y2 = x - d, y - l / 2, x, y - l

    im.line(x1, y1, x2, y2)
    
def square(n):
    
    matrix = generate_square(n)
    dfs_rec(matrix[0][0])
    print_square(matrix, n)

def hexa(n):

    matrix = generate_hexa(n)
    dfs_rec(matrix[0][0])
    print_hexa(matrix, n)

def dfs_rec(point):
    order = [x for x in range(len(point.points))]
    shuffle(order)
    for i in order:
        new_point = point.points[i]
        if len(new_point.ways) == 0:
            point.add_way(new_point)
            new_point.add_way(point)
            dfs_rec(new_point)
    
