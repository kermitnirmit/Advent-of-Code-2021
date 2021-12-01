f = [int(x) for x in open("input.txt").read().strip().split("\n")]
print(sum(int(a > b) for a, b in zip(f[1:], f[:-1])))
print(sum(int(a > b) for a, b in zip(f[3:], f[:-3])))
