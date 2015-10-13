from pickle import dump
import numpy as np

A = np.array([[i+3*j for i in range(3)] for j in range(5)])

f = open("test.txt", "w")

dump(A, f)

f.close
