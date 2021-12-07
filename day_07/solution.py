import statistics
f = [int(x) for x in open("input.txt").read().strip().split(",")]

# Turns out median and mean do the trick.
p1 = int(statistics.median(f))
p2 = int(statistics.mean(f))

def gen_number(n):
    return n * (n+1) // 2

print(sum(abs(a-p1) for a in f))
print(sum(gen_number(abs(a-p2)) for a in f))

print(min([[sum(abs(a-i) for a in f)] for i in range(max(f))]))
print(min([[sum(gen_number(abs(a - i)) for a in f)] for i in range(max(f))]))