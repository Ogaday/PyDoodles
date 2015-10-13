from pickle import load
import numpy as np

f = open("test.txt", "r")

A = load(f)

f.close

print A
