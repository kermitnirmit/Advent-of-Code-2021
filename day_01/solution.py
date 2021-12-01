import numpy as np
import pandas as pd


def count_increases(l):
    return sum(int(a > b) for a, b in zip(l[1:], l[:-1]))


f = [int(x) for x in open("input.txt").read().strip().split("\n")]
print(count_increases(f))
f = [x[0] for x in pd.DataFrame(np.array(f)).rolling(3).sum().values.tolist()]
print(count_increases(f))
