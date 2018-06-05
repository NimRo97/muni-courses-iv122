from math import inf
from SVG import Svg

MAZE = [[0,0,0,1,0,1,1],
        [0,1,0,1,0,1,0],
        [0,1,0,1,1,1,0],
        [1,1,1,1,0,1,0],
        [0,1,0,1,0,1,0],
        [0,1,0,0,0,1,0],
        [1,1,1,1,1,1,1]]

SIMPLE = [[0,1,0],
          [0,1,0],
          [0,0,0]]

class Point():

    def __init__(self, position, points = []):
        self.points = []
        self.ways = []
        self.position = position
        for p in points:
            slef.points.append(p)

    def add_point(self, point, val):
        self.points.append((point, val))

def dfs_rec(point, stack, end, result, length):

    if length > result[0][1]:
        return
    stack.append(point)
    
    if point is end:
        if length < result[0][1]:
            result[0] = stack.copy(), length
            
    for (p, val) in point.points:
        if p not in stack:
            dfs_rec(p, stack, end, result, length + val)

    stack.pop()

def generate_matrix(maze, w, h):

    matrix = [[Point((y, x)) for x in range(w)] for y in range(h)]
    for i in range(w):
        for j in range(h):
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if i + x >= 0 and i + x < w and j + y >=0 and j + y < h:
                    val = 1
                    if maze[i + x][j + y] == 1:
                        val = w * h
                    matrix[i][j].add_point(matrix[i + x][j + y], val)
            matrix[i][j].points.sort(key=lambda x: x[1])
    return matrix

def solve(maze, start, end):
    
    matrix = generate_matrix(maze, len(maze[0]), len(maze))
    result = [(None, inf)]
    dfs_rec(matrix[start[0]][start[1]], [], matrix[end[0]][end[1]],
            result, 0)
    
    LEN = 40
    im = Svg("maze.svg")
    for x in range(len(maze[0])):
        for y in range(len(maze)):
            color = "white"
            if maze[x][y] == 1:
                color = "gray"
            if (x, y) == start or (x, y) == end:
                color = "blue"
            im.rectangle(x * LEN, y * LEN, LEN, LEN, fill=color)
    prew = matrix[start[0]][start[1]]
    for point in result[0][0][1:]:
        x1, y1 = prew.position
        x2, y2 = point.position
        im.line(x1 * LEN + LEN // 2, y1 * LEN - LEN // 2,
                x2 * LEN + LEN // 2, y2 * LEN - LEN // 2, "red")
        prew = point

    im.close()
