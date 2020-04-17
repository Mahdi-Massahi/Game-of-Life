import random
from Graphics import *
from time import sleep

def initialize(_row, _column, prob=0.2):
    _world = []
    for i in range(_row):
        _ = []
        for j in range(_column):
            _.append(1 if random.randint(0, 100) / 100 < prob else 0)
        _world.append(_)
    return _world


def evolution(_world, _row, _column):
    neg = []
    for i in range(_row):
        _ = []
        for j in range(_column):
            lives = 0
            for id in range(i - 1, i + 2):
                for jd in range(j - 1, j + 2):
                    if _world[0 if id == _row else id][0 if jd == _column else jd] == 1:
                        lives += 1
            if _world[i][j] == 1:
                lives -= 1

            _.append(lives)
        neg.append(_)

    for i in range(_row):
        for j in range(_column):
            if _world[i][j] == 1 and (neg[i][j] == 2 or neg[i][j] == 3):
                _world[i][j] = 1
            elif _world[i][j] == 0 and neg[i][j] == 3:
                _world[i][j] = 1
            else:
                _world[i][j] = 0
    return _world


def run(draw_every=1, delay=0.1, prob=0.2):
    world = initialize(row, column, prob)
    ui.draw(world, 1)
    for ev in range(1, 500):
        world = evolution(world, row, column)
        print("\rEvolution:\t", ev, sep = "", end = "")
        if ev % draw_every == 0:
            sleep(delay)
            ui.draw(world, ev)

    ui.wait()


row, column = 150, 150
cell_width = 4
ui = Graphics(row, column, cell_width)
run(50, 0.2, 0.2)
