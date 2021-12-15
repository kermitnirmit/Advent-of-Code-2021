import numpy as np
from heapq import heappush, heappop
f = [x for x in open("input.txt").read().strip().split("\n")]

def solve(targetx, targety):
    board = []
    for line in f:
        a = list(line)
        a = [int(x) for x in a]
        board.append(a)
    board = np.array(board)

    heap = [(0,0,0)]
    seen = {(0,0)}
    dirs = [(-1,0), (1, 0), (0, 1), (0, -1)]

    while heap:
        d, x, y = heappop(heap)
        if x == targetx and y == targety:
            return d
        for dx, dy in dirs:
            nx, ny = dx + x, dy + y
            if 0 <= nx <= targetx and 0 <= ny <= targety:
                i_x, i_xoffset = divmod(nx, len(board))
                i_y, i_yoffset = divmod(ny, len(board[0]))
                nd = (board[i_xoffset][i_yoffset] + i_x + i_y)
                nd = nd % 10 + nd // 10 + d
                if (nx, ny) not in seen:
                    heappush(heap, (nd, nx, ny))
                    seen.add((nx, ny))

print(solve(99,99))
print(solve(499,499))