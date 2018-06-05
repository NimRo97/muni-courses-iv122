MAZE = [[2, 4, 4, 3, 3],
        [2, 3, 3, 2, 3],
        [3, 2, 3, 1, 3],
        [2, 2, 3, 2, 1],
        [1, 4, 4, 4, 0]]

class Point():

    def __init__(self, position, points = []):
        self.points = []
        self.ways = []
        self.position = position
        for p in points:
            slef.points.append(p)

    def add_point(self, point, val):
        self.points.append((point, val))

def dfs_rec(point, stack, end, results, length):
    
    stack.append(point)
    
    if point is end:
        if results and len(results[0]) > len(stack):
            results.clear()
        if not results or len(results[0]) == len(stack):
            results.append(stack.copy())
            
    for (p, val) in point.points:
        if p not in stack:
            dfs_rec(p, stack, end, results, length + val)

    stack.pop()

def generate_matrix(maze, w, h):

    matrix = [[Point((y, x)) for x in range(w)] for y in range(h)]
    for i in range(w):
        for j in range(h):
            n = maze[i][j]
            for x, y in [(n, 0), (0, n), (-n, 0), (0, -n)]:
                if i + x >= 0 and i + x < w and j + y >=0 and j + y < h:
                    matrix[i][j].add_point(matrix[i + x][j + y], 0)
    return matrix

def solve(maze, start, end):
    matrix = generate_matrix(maze, len(maze[0]), len(maze))
    results = []
    dfs_rec(matrix[start[0]][start[1]], [], matrix[end[0]][end[1]], results, 0)
    for result in results:
        print("result:")
        for point in result:
            print(point.position, end = " ")
        print()
    
