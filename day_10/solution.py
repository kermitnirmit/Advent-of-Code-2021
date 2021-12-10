import statistics
f = [x for x in open("input.txt").read().strip().split("\n")]

p1_score = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

open_to_close = {
    "{": "}",
    "[": "]",
    "(": ")",
    "<": ">"
}
part_2_score = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

a = []
p2_scores = []
for i, line in enumerate(f):
    opens = []
    corrupt = False
    for char in line:
        if char in p1_score.keys():
            if open_to_close[opens[-1]] != char and not corrupt:
                a.append(p1_score[char])
                opens.pop(-1)
                corrupt = True
            else:
                opens.pop(-1)
        else:
            opens.append(char)
    if not corrupt:
        rScore = 0
        while len(opens) != 0:
            blob = opens.pop(-1)
            rScore *= 5
            rScore += part_2_score[open_to_close[blob]]
        p2_scores.append(rScore)

print(sum(a))
print(statistics.median(p2_scores))
