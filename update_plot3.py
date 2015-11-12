# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
all_Lists = [list(np.random.randn(30).cumsum()) for i in range(10)]
fig, ax = plt.subplots()
for n, curv in enumerate(all_Lists):
     ax.cla()
     ax.plot(curv)
     plt.pause(0.01)
    
input("Done.")
