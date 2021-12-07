f = [int(x) for x in open("input.txt").read().strip().split(",")]

def gen_number(n):
    return int(n*(n+1)/2)
a1, a2 = [], []
for i in range(len(f)):
    rsum = rsum2 = 0
    for a in f:
        rsum += abs(a - i)
        rsum2 += gen_number(abs(a - i))
    a1.append(rsum)
    a2.append(rsum2)

print(min(a1))
print(min(a2))
