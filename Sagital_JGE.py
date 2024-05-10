#!/usr/bin/env python

"""\
lipm2d.py: A tiny 2d LIPM simulation with matplotlib animation.

- Partial inspiration (beware some bugs atow): <https://github.com/AtsushiSakai/PythonRobotics/blob/808e98133d57426b1e6fbbc2bdc897a196278d7d/Bipedal/bipedal_planner/bipedal_planner.py>
"""

__author__      = "Juan G Victores"
__copyright__   = "Copyright 2024, Planet Earth"

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from time import sleep

MAX_X = 2000
HEIGHT = 0.2*len("Gomez")
print(HEIGHT)
G = 9.8
TIME_DELTA = 0.1 # s

fig, ax = plt.subplots()
ln, = ax.plot([], [], marker = 'o')

def init():
    ax.set_xlim(0, MAX_X)
    ax.set_ylim(-0.2, 1.2)
    return ln,

def animate(args):
    return ln,

class Simulator():
    def __init__(self):
        self.zmp_x = [0, 650, 1400, 2200]
        self.zmp_x_change = [400, 1100, 1900]

        #self.zmp_x = [0, 400, 800, 1200, 1600, 2000]
        #self.zmp_x_change = [200, 600, 1000, 1400, 1800, 2001]

        self.zmp_idx = 0
        self.c_x = self.zmp_x[0] + 0.1 # para que arranque
        self.c_x_dot = 0

    def __call__(self):

        x_dot2 = G / HEIGHT * (self.c_x - self.zmp_x[self.zmp_idx])
        self.c_x += self.c_x_dot * TIME_DELTA
        self.c_x_dot += x_dot2 * TIME_DELTA

        ln.set_data([self.zmp_x[self.zmp_idx], self.c_x], [0, HEIGHT])
        # ln.set_data([180, self.currentTimeStep, 0, self.currentTimeStep], [0, HEIGHT, 0, HEIGHT])

        if self.c_x > self.zmp_x_change[self.zmp_idx]:
            self.zmp_idx += 1

        if self.c_x > MAX_X:
            quit()

        return 1

simulator = Simulator()

def frames():
    while True:
        yield simulator()

ani = FuncAnimation(fig, animate, frames=frames,
                    interval=100, init_func=init,
                    blit=True, save_count=MAX_X)
plt.show()