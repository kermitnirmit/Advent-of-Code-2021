f = [int(x) for x in open("input.txt").read().strip().split(",")]

def gen_number(n):
    return int(n*(n+1)/2)

print(min([[sum(abs(a-i) for a in f)] for i in range(len(f))]))
print(min([[sum(gen_number(abs(a - i)) for a in f)] for i in range(len(f))]))