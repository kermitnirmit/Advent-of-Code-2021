# inp a - Read an input value and write it to variable a.
# add a b - Add the value of a to the value of b, then store the result in variable a.
# mul a b - Multiply the value of a by the value of b, then store the result in variable a.
# div a b - Divide the value of a by the value of b, truncate the result to an integer, then store the result in variable a. (Here, "truncate" means to round the value toward zero.)
# mod a b - Divide the value of a by the value of b, then store the remainder in variable a. (This is also called the modulo operation.)
# eql a b - If the value of a and b are equal, then store the value 1 in variable a. Otherwise, store the value 0 in variable a.

from itertools import permutations
from parse import parse
from collections import defaultdict

# f = open("input.txt").read().strip().split("\n")
f = open("test.txt").read().strip().split("\n")


print(f)

# perms = permutations([1,2,3,4,5,6,7,8,9])
m = -1
minz = 100000000000000
# start = 11111111111111
# start = 95999999999999

for initialzs in range(-500, 500):
    start = 9
    strstart = str(start)
    vars = defaultdict(int)
    vars["z"] = initialzs
    inps = 0
    for line in f:
        print(line)
        input("continue")
        print(vars)
        # print(vars)
        splits = line.split(" ")
        if len(splits) == 2:
            print("found an input")

            vars[splits[1]] = int(strstart[inps])
            # print(vars)
            inps += 1
            # input("cintunue")
        else:
            # print(not splits[2].isalpha())
            if not splits[2].isalpha():
                if splits[0] == "add":
                    vars[splits[1]] += int(splits[2])
                elif splits[0] == "mul":
                    vars[splits[1]] *= int(splits[2])
                elif splits[0] == "div":
                    if int(splits[2]) == 0:
                        break
                    vars[splits[1]] //= int(splits[2])
                elif splits[0] == "mod":
                    if int(splits[2]) == 0:
                        break
                    vars[splits[1]] = vars[splits[1]] % int(splits[2])
                else:
                    vars[splits[1]] = int(vars[splits[1]] == int(splits[2]))
            else:
                if splits[0] == "add":
                    vars[splits[1]] += vars[splits[2]]
                elif splits[0] == "mul":
                    vars[splits[1]] *= vars[splits[2]]
                elif splits[0] == "div":
                    if vars[splits[2]] == 0:
                        break
                    vars[splits[1]] //= vars[splits[2]]
                elif splits[0] == "mod":
                    if vars[splits[2]] <= 0:
                        break
                    vars[splits[1]] = vars[splits[1]] % vars[splits[2]]
                else:
                    vars[splits[1]] = int(vars[splits[1]] == vars[splits[2]])
    # input("continue")
    start -= 1
    while "0" in str(start):
        start -= 1
    # print("not max", start)
    # print(vars)
    # input("continue")
    # if vars["z"] < minz:
    #     minz = vars["z"]
    #     print(minz)
    print(vars)
    if vars["z"] == 0 or start == 1:
        m = max(start, m)
        print(m)
        continue