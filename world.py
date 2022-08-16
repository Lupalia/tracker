#obstacles will be added.

import numpy as np
import matplotlib.pyplot as plt


import matplotlib.animation as animation

#target point

class World():
    def __init__(self):
        self.fig=plt.figure()
        self.ax = plt.axes(projection='3d', autoscale_on=False, xlim=(-10, 10), ylim=(-10, 10),zlim=(-10,10))
        plt.plot(0,0,0,marker="o", markersize=5)
        plt.plot(6,-5,4,marker="o", markersize=5)
        plt.plot(-4,8,-7,marker="o", markersize=5)
        plt.show()
    

    
    def animate(self):
        pass



if __name__=="__main__":
    world=World()