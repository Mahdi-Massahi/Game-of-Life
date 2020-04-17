import random
from Graphics import *
from time import sleep

row, column = 40, 40
cell_width = 10

ui = Graphics(row, column, cell_width, [5, 5, 5, 5])


def initialize(_row, _column, prob=0.2):
    _world = []
    for i in range(_row):
        _ = []
        for j in range(_column):
            _.append(1 if random.randint(0, 100) / 100 < prob else 0)
        _world.append(_)
    return _world


def evolution(_world, _row, _column):
    backup = _world.copy()
    for i in range(_row):
        for j in range(_column):
            lives = 0
            for id in range(i - 1, i + 2):
                if id < 0 or id > _row - 1:
                    continue
                for jd in range(j - 1, j + 2):
                    if jd < 0 or jd > _column - 1:
                        continue
                    if backup[id][jd] == 1:
                        lives += 1

            if backup[i][j] == 1:
                lives -= 1
            if backup[i][j] == 1 and (lives == 2 or lives == 3):
                _world[i][j] = 1
            elif backup[i][j] == 0 and lives == 3:
                _world[i][j] = 1
            else:
                _world[i][j] = 0
    return _world


def run(draw_every=1, delay=0.1):
    world = initialize(row, column, 0.5)
    ui.draw(world, 1)
    for ev in range(1, 100):
        world = evolution(world, row, column)
        if ev % draw_every == 0:
            sleep(delay)
            ui.draw(world, ev)

    ui.wait()


run(1, 0.5)
