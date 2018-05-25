from math import inf

class Svg:

    def __init__(self, filename="image.svg"):
        self.file = open(filename, "w")
        self.lines = []
        self.rectangles = []
        self.file.write('<?xml version="1.0" encoding="UTF-8" ?>\n')

    def tag(self, name, attributes):
        self.file.write('  <' + name)
        for (key, value) in attributes:
            self.file.write(' ' + key + '="' + value + '"')
        self.file.write(' />\n')

    def line(self, x1, y1, x2, y2, stroke="black", width=1):
        self.lines.append((x1, y1, x2, y2, stroke, width))

    def rectangle(self, x, y, w, h, stroke="black", width=1, fill="white"):
        self.rectangles.append((x, y, w, h, stroke, width, fill))

    def flip_y(self):
        self.flip_y_lines()
        self.flip_y_rectangles()

    def flip_y_lines(self):
        lines = self.lines
        for i in range(len(lines)):
            lines[i] = (lines[i][0], - lines[i][1], lines[i][2], - lines[i][3],
                        lines[i][4], lines[i][5])

    def flip_y_rectangles(self):
        rect = self.rectangles
        for i in range(len(rect)):
            rect[i] = (rect[i][0], - rect[i][1], rect[i][2], rect[i][3],
                       rect[i][4], rect[i][5], rect[i][6])

    def write_all_lines(self):
        for (x1, y1, x2, y2, stroke, width) in self.lines:
            self.tag("line", [("x1", str(x1)), ("y1", str(y1)),
                              ("x2", str(x2)), ("y2", str(y2)),
                              ("stroke", stroke),
                              ("stroke-width", str(width))])

    def write_all_rectangles(self):
        for (x, y, w, h, stroke, width, fill) in self.rectangles:
            self.tag("rect", [("x", str(x)), ("y", str(y)),
                              ("width", str(w)), ("height", str(h)),
                              ("stroke", stroke),
                              ("stroke-width", str(width)),
                              ("fill", str(fill))])

    def normalize(self):
        off_x, off_y = self.get_offset()
        self.normalize_all_lines(off_x, off_y)
        self.normalize_all_rectangles(off_x, off_y)

    def get_offset(self):
        
        min_x, min_y = inf, inf
        
        for line in self.lines:
            if line[0] < min_x:
                min_x = line[0]
            if line[2] < min_x:
                min_x = line[2]
            if line[1] < min_y:
                min_y = line[1]
            if line[3] < min_y:
                min_y = line[3]

        for rect in self.rectangles:
            if rect[0] < min_x:
                min_x = rect[0]
            if rect[1] < min_y:
                min_y = rect[1]
                
        return (- min_x, - min_y)

    def normalize_all_lines(self, off_x, off_y):
        lines = self.lines
        for i in range(len(lines)):
            lines[i] = (lines[i][0] + off_x, lines[i][1] + off_y,
                        lines[i][2] + off_x, lines[i][3] + off_y,
                        lines[i][4], lines[i][5])

    def normalize_all_rectangles(self, off_x, off_y):
        rect = self.rectangles
        for i in range(len(rect)):
            rect[i] = (rect[i][0] + off_x, rect[i][1] + off_y, rect[i][2],
                       rect[i][3], rect[i][4], rect[i][5], rect[i][6])

    def get_width(self):
        max_x = -inf
        for line in self.lines:
            if line[0] > max_x:
                max_x = line[0]
            if line[2] > max_x:
                max_x = line[2]
        for rect in self.rectangles:
            if rect[0] + rect[2] > max_x:
                max_x = rect[0] + rect[2]
        return max_x

    def get_height(self):
        max_y = -inf
        for line in self.lines:
            if line[1] > max_y:
                max_y = line[1]
            if line[3] > max_y:
                max_y = line[3]
        for rect in self.rectangles:
            if rect[1] + rect[3] > max_y:
                max_y = rect[1] + rect[3]
        return max_y
        
    def close(self):
        self.flip_y()
        self.normalize()
        self.file.write('<svg xmlns="http://www.w3.org/2000/svg"' +
                        ' version="1.1" width="' + str(self.get_width()) +
                        '" height="' + str(self.get_height()) + '">\n')
        self.write_all_lines()
        self.write_all_rectangles()
        self.file.write("</svg>\n")
        self.file.close()
