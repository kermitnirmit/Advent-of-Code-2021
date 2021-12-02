f = [x.split(" ") for x in open("input.txt").read().strip().split("\n")]
x = prob1y = y = aim = 0
for d, m in f:
    m = int(m)
    if d[0] == "f":
        x += m
        y += m * aim
    elif d[0] == "d":
        aim += m
        prob1y += m
    else:
        aim -= m
        prob1y -= m
print(x * prob1y)
print(x * y)
