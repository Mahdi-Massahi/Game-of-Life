import random

row, column = 10, 10

world = []
for i in range(row):
    _ = []
    for j in range(column):
        _.append(random.randint(0, 1))
    world.append(_)


for i in range(row):
    for j in range(column):
        lives = 0
        for id in range(i - 1, i + 2):
            if id < 0 or id > 9:
                continue
            for jd in range(j - 1, j + 2):
                if jd < 0 or jd > 9:
                    continue
                if world[id][jd] == 1:
                    lives += 1
        if world[i][j] == 1:
            lives -= 1
        if world[i][j] == 1 and (lives == 2 or lives == 3):
            world[i][j] = 1
        elif lives == 3 and world[i][j] == 0:
            world[i][j] = 1
        else:
            world[i][j] = 0


