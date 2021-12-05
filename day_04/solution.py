f = [x for x in open("input.txt").read().strip().split("\n")]

firstLine, boards, i = [int(x) for x in f[0].split(",")], [], 2


class Board:
    def __init__(self, r, c, rows):
        self.r = r
        self.c = c
        self.rows = rows
        self.markedVals = []
        self.bingo = False

    def addRow(self, row):
        self.rows.append(row)

    def markVal(self, val):
        for i, r in enumerate(self.rows):
            for j, c in enumerate(r):
                if c == val:
                    self.markedVals.append((i, j))

    def checkBingo(self):
        for i in range(self.r):
            # if there are enough marked vals in a certain row to equal the length, we have a bingo
            if len(list(filter(lambda x: x[0] == i, self.markedVals))) == self.r:
                self.bingo = True
                return True
            if len(list(filter(lambda x: x[1] == i, self.markedVals))) == self.c:
                self.bingo = True
                return True
        return False

    def findUncheckedAndSum(self):
        rsum = 0
        for i, r in enumerate(self.rows):
            for j, c in enumerate(r):
                if (i, j) not in self.markedVals:
                    rsum += c
        return rsum


currBoard = None

while i < len(f):
    if currBoard is None:
        currBoard = Board(5, 5, [])
    if len(f[i]) == 0:
        boards.append(currBoard)
        currBoard = None
    else:
        currBoard.addRow([int(x.strip()) for x in list(filter(lambda x: len(x) > 0, f[i].split(" ")))])
    i += 1
boards.append(currBoard)

winnersFound = 0
for entry in firstLine:
    for board in list(filter(lambda x: x.bingo is False, boards)):
        board.markVal(entry)
        if board.checkBingo():
            winnersFound += 1
            if winnersFound in [1, 100]:
                print(winnersFound, board.findUncheckedAndSum() * entry)
