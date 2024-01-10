import numpy as np


def generate(p1):
    return np.random.choice([0, 1], size=10000, p=[1 - p1, p1])


def count(seq):
    wins = 0
    for i in range(seq.size - 4):
        if np.sum(seq[i:i + 5]) == 5:
            wins += 1

    return wins


def main(p1):
    seq = generate(p1)
    return count(seq)


print(main(2 / 3))
