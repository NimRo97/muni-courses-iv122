from SVG import Svg
from math import radians, sin, cos

class MyTurtle():

    def __init__(self, name="turtle"):
        self.pen = True
        self.heading = 0
        self.x = 0
        self.y = 0
        self.im = Svg(name+".svg")
        self.color = "black"
        self.stroke = 1

    def pd(self):
        self.pen = True

    def pu(self):
        self.pen = False

    def head(self, n):
        self.heading = n % 360

    def right(self, n):
        self.heading = (self.heading - n) % 360

    def left(self, n):
        self.heading = (self.heading + n) % 360

    def forward(self, n):
        new_x = self.x + cos(radians(self.heading)) * n
        new_y = self.y + sin(radians(self.heading)) * n
        if self.pen:
            self.im.line(self.x, self.y, new_x, new_y, self.color, self.stroke)
        self.x, self.y = new_x, new_y

    def backward(self, n):
        self.right(180)
        self.forward(n)
        self.right(180)

    def begin_fill(self):
        pass

    def end_fill(self):
        pass

    def speed(self, n):
        pass

    def color(self, color):
        self.color = color

    def stroke(self, stroke):
        self.stroke = stroke

    def save(self):
        self.im.close()

    def clear(self):
        self.__init__()
        
