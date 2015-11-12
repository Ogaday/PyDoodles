# coding: utf-8
import time
import numpy as np
import matplotlib.pyplot as plt
plt.axis([0,1000,0,1])
plt.ion
plt.ion()
plt.show()
for i in range(100):
    y=np.random.random()
    plt.scatter(i,y)
    plt.draw()
    plt.pause(0.05)

input()
