import random

def main():
    probability = random.random()
    favourite = "dogs"  # change this
    if probability < 0.1:
        favourite = "cats"
    if 0.1 < probability < 0.2:
        favourite = "bats"
    print("I love " + favourite)


main()
