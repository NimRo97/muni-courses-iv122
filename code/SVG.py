class Svg:

    def __init__(self, filename="image.svg"):
        self.file = open(filename, "w")
        self.lines = []
        self.file.write('<?xml version="1.0" encoding="UTF-8" ?>\n')

    def tag(self, name, attributes):
        self.file.write('  <' + name)
        for (key, value) in attributes:
            self.file.write(' ' + key + '="' + value + '"')
        self.file.write(' />\n')

    def line(self, x1, y1, x2, y2, stroke="black", width=1):
        self.lines.append((x1, y1, x2, y2, stroke, width))

    def flip_y(self):
        self.flip_y_lines()

    def flip_y_lines(self):
        lines = self.lines
        for i in range(len(lines)):
            lines[i] = (lines[i][0], - lines[i][1], lines[i][2], - lines[i][3],
                        lines[i][4], lines[i][5])

    def write_all_lines(self):
        for (x1, y1, x2, y2, stroke, width) in self.lines:
            self.tag("line", [("x1", str(x1)), ("y1", str(y1)),
                              ("x2", str(x2)), ("y2", str(y2)),
                              ("stroke", stroke),
                              ("stroke-width", str(width))])

    def normalize(self):
        off_x, off_y = self.get_offset()
        self.normalize_all_lines(off_x, off_y)

    def get_offset(self):
        min_x = self.lines[0][0]
        min_y = self.lines[0][1]
        for line in self.lines:
            if line[0] < min_x:
                min_x = line[0]
            if line[2] < min_x:
                min_x = line[2]
            if line[1] < min_y:
                min_y = line[1]
            if line[3] < min_y:
                min_y = line[3]
        return (- min_x, - min_y)

    def normalize_all_lines(self, off_x, off_y):
        lines = self.lines
        for i in range(len(lines)):
            lines[i] = (lines[i][0] + off_x, lines[i][1] + off_y,
                        lines[i][2] + off_x, lines[i][3] + off_y,
                        lines[i][4], lines[i][5])

    def get_width(self):
        max_x = self.lines[0][0]
        for line in self.lines:
            if line[0] > max_x:
                max_x = line[0]
            if line[2] > max_x:
                max_x = line[2]
        return max_x

    def get_height(self):
        max_y = self.lines[0][1]
        for line in self.lines:
            if line[1] > max_y:
                max_y = line[1]
            if line[3] > max_y:
                max_y = line[3]
        return max_y
        
    def close(self):
        self.flip_y()
        self.normalize()
        self.file.write('<svg xmlns="http://www.w3.org/2000/svg"' +
                        ' version="1.1" width="' + str(self.get_width()) +
                        '" height="' + str(self.get_height()) + '">\n')
        self.write_all_lines()
        self.file.write("</svg>\n")
        self.file.close()
