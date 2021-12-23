# Player 1 starting position: 6
# Player 2 starting position: 9
from collections import defaultdict

p1x = 6
# p1x = 4
p1score = 0
p2x = 9
# p2x = 8
p2score = 0
dcount = 0
nd = 1
while True:
    #     p1 dice
    roll = 0
    for i in range(3):
        roll += nd
        nd += 1
        if nd == 101:
            nd = 1
    dcount += 3
    p1x += roll
    while p1x > 10:
        p1x -= 10
    # p1 move
    p1score += p1x
    if p1score >= 1000:
        print(dcount * p2score)
        break
    roll = 0
    for i in range(3):
        roll += nd
        nd += 1
        if nd == 101:
            nd = 1
    dcount += 3
    p2x += roll
    while p2x > 10:
        p2x -= 10
    # p1 move
    p2score += p2x
    if p2score >= 1000:
        print(dcount * p1score)
        break

# p2
p1x = 6
# p1x = 4
p1score = 0
p2x = 9
# p2x = 8
p2score = 0
nd = 1
# gameState = (6,0,9,0)

def move(orig, roll):
    orig += roll
    while orig > 10:
        orig -= 10
    return orig

rf = [(3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1)]

def solve(p1, t1, p2, t2):
    if t2 <= 0:
        return (0, 1)  # p2 has won (never p1 since p1 about to move)

    w1, w2 = 0, 0
    for (r, f) in rf:
        c2, c1 = solve(p2, t2, (p1 + r) % 10, t1 - 1 - (p1 + r) % 10)  # p2 about to move
        w1, w2 = w1 + f * c1, w2 + f * c2

    return w1, w2
# gs = p1x, p1s, p2x, p2s, turn 0/1 for player 1/2
gameState = (6,0,9,0, 0)

# print(0 ^ 1 ^ 1)
p1win = 0
p2win = 0
states = {gameState: 1}

while len(states.keys()) > 0:
    nMap = defaultdict(int)
    for (p1x, p1s, p2x, p2s, turn),v in states.items():
        if p1s >= 21:
            p1win += v
        elif p2s >= 21:
            p2win += v
        elif turn == 0:
            for r,f in rf:
                newGameState = (move(p1x, r), p1s + move(p1x, r), p2x, p2s, turn ^ 1)
                nMap[newGameState] += v * f
        else:
            for r,f in rf:
                newGameState = (p1x, p1s, move(p2x, r), p2s + move(p2x, r), turn ^ 1)
                nMap[newGameState] += v * f
    states = nMap
print(max(p1win, p2win))
