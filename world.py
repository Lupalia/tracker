#obstacles will be added.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

import matplotlib.animation as animation


class World():
    def __init__(self):
        self.fig=plt.figure()
        self.ax = plt.axes(projection='3d', autoscale_on=False, xlim=(-10, 10), ylim=(-10, 10))
        plt.show()
    def animate(self):
        pass



if __name__=="__main__":
    world=World()