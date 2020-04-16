from graphics import *


class Graphics:

    def __init__(self, row, col, box_width, margin):
        self.width = box_width*row + margin[1] + margin[3]
        self.height = box_width*col + margin[0] + margin[2]
        self.row = row
        self.col = col
        self.box_width = box_width
        self.margin = margin
        # self.win = GraphWin("Game of Life", self.width, self.height)
        self.backgroundFill = color_rgb(80, 80, 80)
        self.cellFill = color_rgb(0, 128, 128)
        self.cellOutline = color_rgb(20, 20, 20)

    def draw(self, world):
        self.win = GraphWin("Game of Life", self.width, self.height)
        self.win.setBackground(self.backgroundFill)
        for y, row in enumerate(world):
            for x, cell in enumerate(row):
                upper_left = Point(self.margin[3] + x*self.box_width,
                                   self.margin[0] + y*self.box_width)
                lower_right = Point(self.margin[3] + (x+1)*self.box_width,
                                    self.margin[0] + (y+1)*self.box_width)
                c = Rectangle(upper_left, lower_right)
                if cell:
                    c.setFill(self.cellFill)
                else:
                    c.setFill(self.backgroundFill)

                c.setOutline(self.cellOutline)
                c.draw(self.win)

    def wait(self):
        self.win.getMouse()
        self.win.close()
