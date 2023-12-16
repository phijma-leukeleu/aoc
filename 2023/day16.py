with open("day16_input.txt") as f:
    grid = f.read().splitlines()

SIZE = len(grid[0])


def get_energized_score(start):
    beams = [start]
    visited = set()

    def move(beam):
        retval = []
        col, row, direction = beam
        visited.add(beam)

        if grid[row][col] == "-" and direction in ["U", "D"]:
            if col - 1 >= 0:
                retval.append((col - 1, row, "L"))
            if col + 1 <= SIZE - 1:
                retval.append((col + 1, row, "R"))
        elif grid[row][col] == "|" and direction in ["L", "R"]:
            if row - 1 >= 0:
                retval.append((col, row - 1, "U"))
            if row + 1 <= SIZE - 1:
                retval.append((col, row + 1, "D"))
        elif grid[row][col] == "/":
            if direction == "U":
                if col + 1 <= SIZE - 1:
                    retval.append((col + 1, row, "R"))
            elif direction == "D":
                if col - 1 >= 0:
                    retval.append((col - 1, row, "L"))
            elif direction == "L":
                if row + 1 <= SIZE - 1:
                    retval.append((col, row + 1, "D"))
            elif direction == "R":
                if row - 1 >= 0:
                    retval.append((col, row - 1, "U"))
        elif grid[row][col] == "\\":
            if direction == "U":
                if col - 1 >= 0:
                    retval.append((col - 1, row, "L"))
            elif direction == "D":
                if col + 1 <= SIZE - 1:
                    retval.append((col + 1, row, "R"))
            elif direction == "L":
                if row - 1 >= 0:
                    retval.append((col, row - 1, "U"))
            elif direction == "R":
                if row + 1 <= SIZE - 1:
                    retval.append((col, row + 1, "D"))
        else:
            if direction == "U":
                if row - 1 >= 0:
                    retval.append((col, row - 1, direction))
            elif direction == "D":
                if row + 1 <= SIZE - 1:
                    retval.append((col, row + 1, direction))
            elif direction == "L":
                if col - 1 >= 0:
                    retval.append((col - 1, row, direction))
            elif direction == "R":
                if col + 1 <= SIZE - 1:
                    retval.append((col + 1, row, direction))

        return retval

    while beams:
        b = beams.pop()
        result = move(b)
        for r in result:
            if r not in visited:
                beams.append(r)

    return len({(x, y) for x, y, _ in visited})


print(f"Part 1: {get_energized_score((0, 0, 'R'))}")


scores = set()
for i in range(SIZE):
    start = (i, 0, "D")
    scores.add(get_energized_score(start))
for i in range(SIZE):
    start = (0, i, "R")
    scores.add(get_energized_score(start))
for i in range(SIZE):
    start = (i, SIZE - 1, "U")
    scores.add(get_energized_score(start))
for i in range(SIZE):
    start = (SIZE - 1, i, "L")
    scores.add(get_energized_score(start))

print(f"Part 2: {max(scores)}")
