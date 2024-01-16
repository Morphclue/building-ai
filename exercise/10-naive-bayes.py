import numpy as np

p1 = [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6]
p2 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]


def roll(loaded):
    if loaded:
        print("rolling a loaded die")
        p = p2
    else:
        print("rolling a normal die")
        p = p1

    sequence = np.random.choice(6, size=10, p=p) + 1
    for roll in sequence:
        print("rolled %d" % roll)

    return sequence


def bayes(sequence):
    odds = 1.0
    for roll in sequence:
        likelihood = p2[roll - 1] / p1[roll - 1]
        odds *= likelihood
    if odds > 1:
        return True
    else:
        return False


sequence = roll(True)
if bayes(sequence):
    print("I think loaded")
else:
    print("I think normal")
