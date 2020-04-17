import random
from Graphics import *
from time import sleep

row, column = 40, 40
cell_width = 10

ui = Graphics(row, column, cell_width, [5, 5, 5, 5])


def initialize(_row, _column):
    _world = []
    for i in range(_row):
        _ = []
        for j in range(_column):
            _.append(random.randint(0, 1))
        _world.append(_)
    return _world


def evolution(_world):
    _column = len(_world)
    _row = len(_world[0])
    for i in range(_row):
        for j in range(_column):
            lives = 0
            for id in range(i - 1, i + 2):
                if id < 0 or id > _column-1:
                    continue
                for jd in range(j - 1, j + 2):
                    if jd < 0 or jd > _row-1:
                        continue
                    if _world[id][jd] == 1:
                        lives += 1
            if _world[i][j] == 1:
                lives -= 1
            if _world[i][j] == 1 and (lives == 2 or lives == 3):
                _world[i][j] = 1
            elif lives == 3 and _world[i][j] == 0:
                _world[i][j] = 1
            else:
                _world[i][j] = 0

    return _world


def run(draw_every = 1, delay = 0.1):
    world = initialize(row, column)
    ui.draw(world, 1)

    for ev in range(0, 100):
        world = evolution(world)
        if ev % draw_every == 0:
            sleep(delay)
            ui.draw(world, ev)

    ui.wait()


run(1, 0.1)

