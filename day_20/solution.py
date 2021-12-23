f = open("input.txt").read().strip().split("\n")
# f = open("text.txt").read().strip().split("\n")
# f = open("otherTest.txt").read().strip().split("\n")

algo = f[0]

f = f[2:]
print(f)

infbit = int(algo[0] == "#")

lit_pixels = set()

min_i = 0
max_i = len(f)
min_j = 0
max_j = len(f[0])
for i in range(len(f)):
    for j in range(len(f[i])):
        if f[i][j] == "#":
            lit_pixels.add((i,j))

for i in range(min_i -1, max_i + 1):
    builder = ""
    for j in range(min_j -1, max_j + 1):
        if (i, j) in lit_pixels:
            builder += "#"
        else:
            builder += "."
    print(builder)

print(len(lit_pixels))

dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

for q in range(50):
    new_set = set()
    for i in range(min_i - 1, max_i + 2):
        for j in range(min_j - 1, max_j + 2):
            builder = 0
            for dx, dy in dirs:
                builder *= 2
                ni = i + dx
                nj = j + dy
                builder += (int((ni, nj) in lit_pixels) if min_i <= ni <= max_i and min_j <= nj <= max_j else q & 1 & infbit)
                # if (ni, nj) in lit_pixels and min_i <= ni <= max_i and min_j <= nj <= max_j:
                #     builder += 1
                # else:
                #     builder += q & 1 & infbit
            new_pixel = algo[builder]
            if new_pixel == "#":
                new_set.add((i, j))
    lit_pixels = new_set
    min_i -= 1
    max_i += 1
    min_j -= 1
    max_j += 1

print(len(lit_pixels))

#
# for i in range(min_i - 1, max_i + 2):
#     builder = ""
#     for j in range(min_j - 1, max_j + 2):
#         if (i, j) in lit_pixels:
#             builder += "#"
#         else:
#             builder += "."
#     print(builder)
# print("next iteration")