import random
from Graphics import *
from time import sleep
from Patterns import *


def evolution(_world):
    neg = []
    _row = len(_world)
    _column = len(_world[0])
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
            # Any live cell with fewer than two live neighbours, dies
            if _world[i][j] == 1 and neg[i][j] < 2:
                _world[i][j] = 0

            # Any live cell with more than three live neighbours, dies
            if _world[i][j] == 1 and neg[i][j] > 3:
                _world[i][j] = 0

            # Any live cell with two or three live neighbours lives, unchanged, to the next generation.
            if _world[i][j] == 1 and (neg[i][j] == 2 or neg[i][j] == 3):
                _world[i][j] = 1

            # Any dead cell with exactly three live neighbours will come to life.
            if _world[i][j] == 0 and neg[i][j] == 3:
                _world[i][j] = 1

    return _world


def run(init, draw_every = 1, delay = 0.1, gen = 500):
    ui.draw(init, 1)
    for ev in range(1, gen):
        init = evolution(init)
        print("\rEvolution:\t", ev, sep = "", end = "")
        if ev % draw_every == 0:
            sleep(delay)
            ui.draw(init, ev)

    ui.wait()


world = flower # random_world(60, 60, prob = 0.5)
ui = Graphics(len(world), len(world[0]), box_width=12)

run(init = world,
    draw_every = 1,
    delay = 0.3,
    gen = 100)
