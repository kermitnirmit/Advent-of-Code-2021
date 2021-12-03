filteredListMC = filteredListLC = f = [[int(y) for y in list(x)] for x in open("input.txt").read().strip().split("\n")]
l = r = final_p2LC = final_p2MC = 0

for i in range(len(f[0])):
    if len(filteredListMC) == 1:
        final_p2MC = int(''.join(str(x) for x in filteredListMC[0]), 2)
    if len(filteredListLC) == 1:
        final_p2LC = int(''.join(str(x) for x in filteredListLC[0]), 2)
    if final_p2MC > 1 and final_p2LC > 1:
        print("part 2", final_p2MC * final_p2LC)
    mcp1, mcp2, lcp2 = sum(x[i] for x in f), sum(x[i] for x in filteredListMC), sum(x[i] for x in filteredListLC)
    filteredListMC = list(filter(lambda x: x[i] == int(mcp2 >= (len(filteredListMC) / 2)), filteredListMC))
    filteredListLC = list(filter(lambda x: x[i] == int(lcp2 < (len(filteredListLC) / 2)), filteredListLC))
    l, r = (l * 2 + 1, r * 2) if mcp1 >= (len(f) / 2) else (l * 2, r * 2 + 1)
print("part 1", l * r)
