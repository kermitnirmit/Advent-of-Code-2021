f = [[int(y) for y in list(x)] for x in open("input.txt").read().strip().split("\n")]
filteredListMC = filteredListLC = f
l = r = final_p2LC = final_p2MC = 0

for i in range(len(f[0])):
    if len(filteredListMC) == 1:
        final_p2MC = ''.join(str(x) for x in filteredListMC[0])
    if len(filteredListLC) == 1:
        final_p2LC = ''.join(str(x) for x in filteredListLC[0])
    if len(str(final_p2MC)) > 1 and len(str(final_p2LC)) > 1:
        print("part 2", int(final_p2MC, 2) * int(final_p2LC, 2))
    mcp1, mcp2, lcp2 = sum(x[i] for x in f), sum(x[i] for x in filteredListMC), sum(x[i] for x in filteredListLC)
    filteredListMC = list(filter(lambda x: x[i] == int(mcp2 >= (len(filteredListMC) / 2)), filteredListMC))
    filteredListLC = list(filter(lambda x: x[i] == int(lcp2 < (len(filteredListLC) / 2)), filteredListLC))
    l, r = (l * 2 + 1, r * 2) if mcp1 >= (len(f) / 2) else (l*2, r * 2 + 1)
print("part 1", l * r)