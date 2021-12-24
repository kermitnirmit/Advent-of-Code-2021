# inp a - Read an input value and write it to variable a.
# add a b - Add the value of a to the value of b, then store the result in variable a.
# mul a b - Multiply the value of a by the value of b, then store the result in variable a.
# div a b - Divide the value of a by the value of b, truncate the result to an integer, then store the result in variable a. (Here, "truncate" means to round the value toward zero.)
# mod a b - Divide the value of a by the value of b, then store the remainder in variable a. (This is also called the modulo operation.)
# eql a b - If the value of a and b are equal, then store the value 1 in variable a. Otherwise, store the value 0 in variable a.
import functools

f = open("input.txt").read().strip().split("\n")

addx = []
divz = []
addy = []

for i, line in enumerate(f):
    if "add x" in line and "add x z" not in line:
        addx.append(int(line.split(" ")[2]))
    if "div z" in line:
        divz.append(int(line.split(" ")[2]))
    if "add y" in line and i % 18 == 15:
        addy.append(int(line.split(" ")[2]))

print(addx)
print(divz)
print(addy)

# stolen from a reddit comment tysm :D
Zbudget = [26 ** len([x for x in range(len(addx)) if divz[x] == 26 and x >= i]) for i in range(len(divz))]

def go(c, z, w):
    x = addx[c] + (z % 26)
    z = z // divz[c]

    if x != w:
        z *= 26
        z += w + addy[c]
    return z

@functools.lru_cache(maxsize=None)
def solve(monadi, zsofar):
    if monadi == 14:
        if zsofar == 0:
            return [""]
        return []
    if zsofar > Zbudget[monadi]:
        return []
    xbecomes = addx[monadi] + zsofar % 26
    possibleNexts = list(range(1,10))
    if xbecomes in possibleNexts:
        possibleNexts = [xbecomes]

    r = []
    for pnext in possibleNexts:
        newz = go(monadi, zsofar, pnext)
        nexts = solve(monadi + 1, newz)
        for n in nexts:
            r.append(str(pnext) + n)
    return r

solns = [int(x) for x in solve(0, 0)]
print(max(solns))
print(min(solns))
