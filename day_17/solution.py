from tqdm import trange
f = open("input.txt").read().strip().split("\n")
"""
The probe's x position increases by its x velocity.
The probe's y position increases by its y velocity.
Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
Due to gravity, the probe's y velocity decreases by 1.
"""
max_ys = []
for q in trange(1, 1000):
    for w in range(-156, 1000):
        x,y = 0,0
        dx = q
        dy = w
        y_pos = []
        for _ in range(2000):
            x += dx
            y += dy
            dy -= 1
            if dx > 0:
                dx -= 1
            elif dx < 0:
                dx += 1
            if dx > 0 and x > 151:
                break
            if dx < 0 and x < 94:
                break
            if dy < 0 and y < -156:
                break
            if dx == 0 and not (94 <= x <= 151):
                break
            y_pos.append(y)
            if 94 <= x <= 151 and -156 <= y <= -103:
                max_ys.append(max(y_pos))
                break
print(max(max_ys))
print(len(max_ys))

