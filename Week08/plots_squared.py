# This is to demonstrate matplot lib
# by ploting y = x squared
# you could use seaborn
# Author: Andrew Beatty

import numpy as np

import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints #multiply each entry by itself

plt.plot(xpoints, ypoints)
plt.show()
