f = [x for x in open("input.txt").read().strip().split("\n")]
x = 0
prob1y = 0
y = 0
aim = 0
for a in f:
    dir, dist = a.split(" ")
    dist = int(dist)
    if dir == "forward":
        x += dist
        y += dist * aim
    if dir == "down":
        aim += dist
        prob1y += dist
    if dir == "up":
        aim -= dist
        prob1y -= dist
print(x * prob1y)
print(x * y)


