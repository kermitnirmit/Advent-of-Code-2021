f = [list(x) for x in open("input.txt").read().strip().split("\n")]
filteredListMC = filteredListLC = f
l = r = final_p2LC = finalp2MC = 0

for i in range(len(f[0])):
    if len(filteredListMC) == 1:
        finalp2MC = ''.join(x for x in filteredListMC[0])
    if len(filteredListLC) == 1:
        final_p2LC = ''.join(x for x in filteredListLC[0])
    if len(str(finalp2MC)) > 5 and len(str(final_p2LC)) > 5:
        print("part 2", int(finalp2MC, 2) * int(final_p2LC, 2))
    mcp1 = sum(int(x[i]) for x in f)
    mcp2 = sum(int(x[i]) for x in filteredListMC)
    lcp2 = sum(int(x[i]) for x in filteredListLC)

    if mcp2 >= (len(filteredListMC) / 2):
        filteredListMC = list(filter(lambda x: x[i] == '1', filteredListMC))
    else:
        filteredListMC = list(filter(lambda x: x[i] == '0', filteredListMC))
    if lcp2 < (len(filteredListLC) / 2):
        filteredListLC = list(filter(lambda x: x[i] == '1', filteredListLC))
    else:
        filteredListLC = list(filter(lambda x: x[i] == '0', filteredListLC))

    if mcp1 >= (len(f) / 2):
        l *= 2
        l += 1
        r *= 2
        f = list(filter(lambda x: x[i] == "1", f))
    else:
        l *= 2
        r *= 2
        r += 1
        f = list(filter(lambda x: x[i] == "0", f))
print("part 1", l * r)