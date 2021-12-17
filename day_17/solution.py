f = open("input.txt").read().strip().split("\n")
"""
The probe's x position increases by its x velocity.
The probe's y position increases by its y velocity.
Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
Due to gravity, the probe's y velocity decreases by 1.
"""
xmin, xmax, ymin, ymax = 94, 151, -156, -103
max_ys = []
for q in range(1, xmax + 1):
    for w in range(ymin, ymin * -1):
        x,y = 0, 0
        dx = q
        dy = w
        y_pos = -100000
        while True:
            x += dx
            y += dy
            dy -= 1
            if dx > 0:
                dx -= 1
            elif dx < 0:
                dx += 1
            if (dx > 0 and x > xmax) \
                    or (dx < 0 and x < xmin) \
                    or (dy < 0 and y < ymin) \
                    or (dx == 0 and not (xmin <= x <= xmax)):
                break
            y_pos = max(y, y_pos)
            if xmin <= x <= xmax and ymin <= y <= ymax:
                max_ys.append(y_pos)
                break
print(max(max_ys))
print(len(max_ys))

