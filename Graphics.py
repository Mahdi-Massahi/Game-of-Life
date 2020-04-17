from ezgraphics import *


class Graphics:

    def __init__(self, row, col, box_width):

        self.margin = [5, 5, 5, 5]
        self.width = box_width*col + self.margin[1] + self.margin[3]
        self.height = box_width*row + self.margin[0] + self.margin[2]
        self.row = row
        self.col = col
        self.box_width = box_width
        self.win = GraphicsWindow(self.width, self.height)
        self.backgroundFill = [80, 80, 80]
        self.cellFill = [100, 150, 150]
        self.canvas = self.win.canvas()
        self.canvas.setBackground(*self.backgroundFill)
        self.win.setTitle("Game of Life")

    def draw(self, world, ev = ""):
        self.win.setTitle("Game of Life " + str(ev))
        self.canvas.clear()
        self.canvas.setOutline(*self.backgroundFill)
        for y, row in enumerate(world):
            for x, cell in enumerate(row):
                if cell:
                    self.canvas.setFill(*self.cellFill)
                    _ = [self.margin[3] + x*self.box_width, self.margin[0] + y*self.box_width]
                    self.canvas.drawRectangle(_[0], _[1], self.box_width, self.box_width)

    def clear(self):
        self.canvas.clear()

    def wait(self):
        self.win.wait()
