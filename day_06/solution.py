from collections import Counter
# f = [int(x) for x in "3,4,3,1,2".split(",")]
f = [int(x) for x in "1,1,3,5,3,1,1,4,1,1,5,2,4,3,1,1,3,1,1,5,5,1,3,2,5,4,1,1,5,1,4,2,1,4,2,1,4,4,1,5,1,4,4,1,1,5,1,5,1,5,1,1,1,5,1,2,5,1,1,3,2,2,2,1,4,1,1,2,4,1,3,1,2,1,3,5,2,3,5,1,1,4,3,3,5,1,5,3,1,2,3,4,1,1,5,4,1,3,4,4,1,2,4,4,1,1,3,5,3,1,2,2,5,1,4,1,3,3,3,3,1,1,2,1,5,3,4,5,1,5,2,5,3,2,1,4,2,1,1,1,4,1,2,1,2,2,4,5,5,5,4,1,4,1,4,2,3,2,3,1,1,2,3,1,1,1,5,2,2,5,3,1,4,1,2,1,1,5,3,1,4,5,1,4,2,1,1,5,1,5,4,1,5,5,2,3,1,3,5,1,1,1,1,3,1,1,4,1,5,2,1,1,3,5,1,1,4,2,1,2,5,2,5,1,1,1,2,3,5,5,1,4,3,2,2,3,2,1,1,4,1,3,5,2,3,1,1,5,1,3,5,1,1,5,5,3,1,3,3,1,2,3,1,5,1,3,2,1,3,1,1,2,3,5,3,5,5,4,3,1,5,1,1,2,3,2,2,1,1,2,1,4,1,2,3,3,3,1,3,5".split(",")]

def solve(end=80):
    c = Counter(f)
    for i in range(end):
        if 0 not in c:
            zeros = 0
        else:
            zeros = c[0]
        new_counter = {}
        for k,v in c.items():
            new_counter[k-1] = v
        if zeros > 0:
            if 6 in new_counter:
                new_counter[6] += new_counter[-1]
            else:
                new_counter[6] = new_counter[-1]
        new_counter[8] = zeros
        newer_counter = {}
        for k,v in new_counter.items():
            if k > -1:
                newer_counter[k] = v
        c = newer_counter
    count = 0
    for k,v in c.items():
        count += v
    return count
print("part 1:", solve(80))
print("part 2:", solve(256))

# For Part 1 I simulated the array because it was faster to type.
#
# f = np.array(f)
#
# toAdd = 0
# last_len = len(f)
# for i in range(80):
#     if toAdd > 0:
#         f = np.pad(f, (0, toAdd), 'constant', constant_values=(0, 9))
#     f -= 1
#     toAdd = (f == 0).sum()
#     f = np.where(f == -1, 6, f)
#     print(i +1, len(f), last_len, len(f) - last_len)
#     last_len = len(f)
# print(len(f))


