import numpy as np

x_train = np.random.rand(10, 3)
x_test = np.random.rand(3)


def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi) ** 2
    return np.sqrt(sum)


def nearest(x_train, x_test):
    nearest = -1
    min_distance = np.Inf
    for i in range(len(x_train)):
        distance = dist(x_train[i], x_test)
        if distance < min_distance:
            min_distance = distance
            nearest = i
    print(nearest)


nearest(x_train, x_test)
