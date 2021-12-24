from collections import defaultdict

f = open("input.txt").read().strip().split("\n\n")
scanners = []


def get_dist(a, b):
    return sum(abs(q - w) for q, w in zip(a, b))


def roll(v): return v[0], v[2], -v[1]


def turn(v): return -v[1], v[0], v[2]


def rotate(v):
    rotations = []
    for cycle in range(2):
        for step in range(3):  # Yield RTTT 3 times
            v = roll(v)
            rotations.append(v)  # Yield R
            for i in range(3):  # Yield TTT
                v = turn(v)
                rotations.append(v)
        v = roll(turn(roll(v)))  # Do RTR
    return rotations


def pointadd(a, b):
    return tuple(q + w for q, w in zip(a, b))


def pointdiff(a, b):
    return tuple(q - w for q, w in zip(a, b))


for num, scannerstuff in enumerate(f):
    lines = scannerstuff.split("\n")[1:]
    r = list(tuple(map(int, x.split(","))) for x in lines)
    scanners.append(r)

homebase = scanners.pop(0)
coords = [(0, 0, 0)]
ocean = set(homebase)

while scanners:
    print("# of scanners remaining", len(scanners))
    curr = scanners.pop(0)
    found = False
    for rot in range(24):
        o = defaultdict(int)
        for elem in ocean:  # looking at every point that's already there in the world
            for point in curr:  # looking at every beacon on this scanner
                rot_point = rotate(point)[rot]  # rotate it the way it should be
                offset = pointdiff(rot_point, elem)  # find the diff from the existing point to this rotated beacon
                o[offset] += 1
                # increment the number of points that are exactly this offset away from existing
                # points with this rotation
        for off, c in o.items():
            if c >= 12:  # found 12 matches, this is the rotation that we need to use.
                found = True
                new_loc = pointdiff((0, 0, 0), off)  # this scanner at the opposite of the offset
                coords.append(new_loc)  # we need all scanner locations for p2
                for point in curr:
                    rot_point = rotate(point)[rot]  # gotta rotate the point back to the way it should be
                    ocean.add(pointadd(rot_point, new_loc))  # add it to the "world"
        continue
    if not found:  # don't have enough points in the world to match this scanner yet - put it back for later
        scanners.append(curr)

print(len(ocean))
scanner_locs = list(set(coords))
dists = [get_dist(q, w) for q in scanner_locs for w in scanner_locs]
print(max(dists))
