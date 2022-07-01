from random import random, seed


def approximate_pi(r: int, lim: int):
    total, inside = 0, 0
    for i in range(lim):
        x = random() * 2
        y = random() * 2
        total += 1
        if ((x - 1) ** 2 + (y - 1) ** 2) <= r**2:
            inside += 1

    pi_aprox = inside / total * 4
    return pi_aprox


seed(0)
print(approximate_pi(1, 1000000))
