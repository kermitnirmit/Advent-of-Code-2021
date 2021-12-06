import numpy as np
import parse

f = open("input.txt").read().strip().split("\n")


def fill_lines(diagonals_ok=False):
    arr = np.zeros((1000, 1000))
    for line in f:
        l_x, l_y, r_x, r_y = tuple(parse.parse('{:d},{:d} -> {:d},{:d}', line).fixed)
        if l_x == r_x or r_y == l_y:
            arr[min(l_y, r_y): max(l_y, r_y) + 1, min(l_x, r_x):max(l_x, r_x) + 1] += 1
        if abs(l_x - r_x) == abs(l_y - r_y) and diagonals_ok:
            d_x = -1 if l_x > r_x else 1
            d_y = -1 if l_y > r_y else 1
            n_x = l_x
            n_y = l_y
            while n_x != r_x and n_y != r_y:
                arr[n_y, n_x] += 1
                n_y += d_y
                n_x += d_x
            arr[n_y, n_x] += 1
    print((arr > 1).sum())


fill_lines(False)
fill_lines(True)
