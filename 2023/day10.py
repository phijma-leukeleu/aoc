# A mess 😊

with open("day10_input.txt") as f:
    grid_input = f.read().splitlines()


dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# Part 1
PIPE_MAPPING = {
    "|": (1, 0, 1, 0),
    "-": (0, 1, 0, 1),
    "L": (1, 1, 0, 0),
    "J": (1, 0, 0, 1),
    "7": (0, 0, 1, 1),
    "F": (0, 1, 1, 0),
    ".": (0, 0, 0, 0),
    "S": (1, 1, 1, 1),
}

grid = [[PIPE_MAPPING[cell] for cell in row] for row in grid_input]


def is_connected(p1, p2, direction):
    if direction == (0, -1):
        return p1[0] and p2[2]
    if direction == (1, 0):
        return p1[1] and p2[3]
    if direction == (0, 1):
        return p1[2] and p2[0]
    if direction == (-1, 0):
        return p1[3] and p2[1]


current = None
for j, row in enumerate(grid):
    if (1, 1, 1, 1) in row:
        current = row.index((1, 1, 1, 1)), j


visited = {(current[0], current[1]): (0, 0)}
while True:
    for i, j in dirs:
        x, y = current[0] + i, current[1] + j
        if x < 0 or y < 0:
            continue

        try:
            p1 = grid[current[1]][current[0]]
            p2 = grid[y][x]
        except IndexError:
            continue

        if (x, y) not in visited and is_connected(p1, p2, (i, j)):
            current = x, y
            visited[(x, y)] = i, j
            break
    else:
        break


print(f"Part 1: {int(len(visited) / 2)}")


inside = set()
for x, y in visited:
    r, s = visited[(x, y)]

    if (r, s) == (0, 0):
        continue

    # Shortcut, just assume we're going right.....
    if (r, s) == (1, 0):
        to_check = [(x, y + 1)]
        if grid_input[y][x] == "J":
            to_check.append((x + 1, y))
    elif (r, s) == (0, 1):
        to_check = [(x - 1, y)]
        if grid_input[y][x] == "L":
            to_check.append((x, y + 1))
    elif (r, s) == (-1, 0):
        to_check = [(x, y - 1)]
        if grid_input[y][x] == "F":
            to_check.append((x - 1, y))
    elif (r, s) == (0, -1):
        to_check = [(x + 1, y)]
        if grid_input[y][x] == "7":
            to_check.append((x, y - 1))
    else:
        raise Exception("Shouldn't happen")

    to_check = [r for r in to_check if r not in visited and r not in inside]

    try:
        group = set(to_check)
        while to_check:
            current = to_check.pop()
            for dx, dy in dirs:
                x, y = current[0] + dx, current[1] + dy
                if (x, y) not in group and (x, y) not in visited:
                    group.add((x, y))
                    to_check.append((x, y))
        for g in group:
            inside.add(g)
    except IndexError:
        pass


print(f"Part 2: {len(inside)}")
