import math
import random

w = [.05, random.random() / 3, random.random() / 3]
h = [1. + math.sin(1 + x / .6) * w[0] + math.sin(-.3 + x / 9.) * w[1] + math.sin(-.2 + x / 30.) * w[2] for x in
     range(100)]


def climb(x, h):
    summit = False

    while not summit:
        best_step = 0

        for step in range(-5, 6):
            if h[x + step] > h[x + best_step]:
                best_step = step
        if best_step == 0:
            break
        x += best_step
    return x


def main(h):
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    return x0, x


main(h)
