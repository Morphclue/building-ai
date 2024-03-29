import math
import numpy as np

x = np.array([4, 3, 0])
c1 = np.array([-.5, .1, .08])
c2 = np.array([-.2, .2, .31])
c3 = np.array([.5, -.1, 2.53])


def sigmoid(z):
    return 1 / (1 + math.exp(-z))


print(sigmoid(np.dot(x, c1)))
print(sigmoid(np.dot(x, c2)))
print(sigmoid(np.dot(x, c3)))
