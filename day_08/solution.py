from collections import defaultdict

f = [x for x in open("input.txt").read().strip().split("\n")]
counter = 0
q = []
for index, line in enumerate(f):
    nums = defaultdict(str)
    first, second = line.split(" | ")
    first = first.split(" ")
    second = second.split(" ")
    segments = [""] * 7
    segments_locked = 0
    while segments_locked != 7:
        rightSide, leftMiddle, top = None, None, None
        for a in first:
            if len(a) == 7:
                nums[8] = a
            if len(a) == 3:
                nums[7] = a
            if len(a) == 2:
                nums[1] = a
            if len(a) == 4:
                nums[4] = a
        rightSide = list(set(nums[1]))
        if len(set(nums[7]) - set(nums[1])) > 0:
            top = (set(nums[7]) - set(nums[1])).pop()
            segments[0] = str(top)
        leftMiddle = list(set(nums[4]) - set(nums[1]))
        for a in first:
            if len(a) == 6:
                if rightSide is not None:
                    for i, r in enumerate(rightSide):
                        if r not in a and segments[1] == "":
                            segments[1] = r
                            if i == 0:
                                segments[2] = rightSide[1]
                            else:
                                segments[2] = rightSide[0]
                            segments_locked += 2
                            nums[6] = a
                if leftMiddle is not None:
                    r = list(set(list(a)) - set(nums[7]) - set(leftMiddle))
                    if len(r) == 1:
                        nums[9] = a
                        segments[3] = str(r.pop())
                        segments_locked += 1
                if len("".join(segments[0:4])) == 4 and segments[6] == "":
                    r = list(set(set(list(a)) - set(segments[0:4])))
                    leftSide = r
                    leftTop = set(leftMiddle) & set(leftSide)
                    if len(leftTop) == 1:
                        nums[0] = a
                        segments[5] = list(leftTop)[0]
                        segments[4] = list(set(leftSide) - leftTop)[0]
                        segments[6] = list(set(leftMiddle) - leftTop)[0]
                        segments_locked += 3
            if len(set(nums[7]) - set(nums[1])) > 0:
                top = (set(nums[7]) - set(nums[1])).pop()
                segments[0] = str(top)
            leftMiddle = list(set(nums[4]) - set(nums[1]))
    if segments_locked == 7:
        nums[2] = segments[0] + segments[1] + segments[6] + segments[3] + segments[4]
        nums[3] = segments[0] + segments[1] + segments[6] + segments[2] + segments[3]
        nums[5] = segments[0] + segments[5] + segments[6] + segments[2] + segments[3]
        inv_map = {v: k for k, v in nums.items()}
        otherC = 0
        for number in second:
            if len(number) in [7, 3, 2, 4]:
                counter += 1
            otherC *= 10
            for k in inv_map.keys():
                if set(k) == set(number):
                    otherC += inv_map[k]
        q.append(otherC)

print(counter)
print(sum(q))
