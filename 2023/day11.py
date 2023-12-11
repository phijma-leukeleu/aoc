from itertools import combinations

with open("day11_input.txt") as f:
    grid = f.read().splitlines()

space = [list(g) for g in grid]

expand_horizontal = []
expand_vertical = []

for i, row in enumerate(space):
    if all(c == "." for c in row):
        expand_vertical.append(i)
for j, col in enumerate(list(zip(*space))):
    if all(c == "." for c in col):
        expand_horizontal.append(j)

galaxies = []
for i, row in enumerate(space):
    for j, col in enumerate(row):
        if col == "#":
            galaxies.append((j, i))

for expand_factor in [1, 999_999]:
    total = 0
    for c in combinations(galaxies, 2):
        g1, g2 = c
        x1, x2 = g1
        y1, y2 = g2
        distance = abs(x1 - y1) + abs(x2 - y2)
        for i in expand_horizontal:
            if x1 < i < y1 or y1 < i < x1:
                distance += expand_factor
        for j in expand_vertical:
            if x2 < j < y2 or y2 < j < x2:
                distance += expand_factor
        total += distance

    print(f"Part {1 if expand_factor == 1 else 2}: {total}")
