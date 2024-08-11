
import matplotlib.pyplot as plt

import numpy as np

xpoints = np.array([0,5])
ypoints = np.array([0,199])

plt.plot(xpoints, ypoints)
plt.show()

class Display():

    def __init__(self):
        self.xpoints = None
        self.ypoints = None

    def passData_XY(self, xpoints, ypoints):
        self.xpoints = xpoints
        self.ypoints = ypoints

    def show(self):
        plt.plot(self.xpoints, self.ypoints)
        plt.show






