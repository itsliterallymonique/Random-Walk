#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RANDOM WALK PROGRAM

By: it's literally monique
"""
# import necessary libraries
import matplotlib.pyplot as plt
import random

# number of iterations
i = 10000

# random walk function
def randoWalk(iteration):
    x = 0
    y = 0
    y_coord = [0]
    x_coord = [0]
    for i in range(iteration):
        # random decimal number from 0 to 1
        movement = random.random()
        if movement < 0.5:
            y += 1
            x += 1
        if movement > 0.5:
            y -= 1
            x += 1
        y_coord.append(y)
        x_coord.append(x)
    
    return [x_coord, y_coord]

# run random walk function
randomWalk = randoWalk(i)

# plot function
plt.plot(randomWalk[0],randomWalk[1])
plt.title("Random Walk")
plt.show()