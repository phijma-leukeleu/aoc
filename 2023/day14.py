with open("day14_input.txt") as f:
    grid = f.read().splitlines()


# Part 1
grid = list(zip(*grid))

score = 0
for row in grid:
    length = len(row)
    current_boundary = 0
    for i, char in enumerate(row):
        if char == "#":
            current_boundary = i + 1
        if char == "O":
            score += length - current_boundary
            current_boundary += 1
print(f"Part 1: {score}")


# Part 2
with open("day14_input.txt") as f:
    grid = f.read().splitlines()


def grid_to_tuples(g):
    return tuple([tuple(r) for r in g])


CYCLES = 1_000_000_000
count = 0
visited = dict()

iteration_count = CYCLES  # When we find a duplicate grid, we overwrite this
while count < iteration_count:
    count += 1

    for orientation in ["N", "W", "S", "E"]:
        if orientation == "N":
            grid = list(zip(*grid))
        if orientation == "S":
            grid = list(zip(*grid))
            grid = [row[::-1] for row in grid]
        if orientation == "E":
            grid = [row[::-1] for row in grid]

        for j, row in enumerate(grid):
            length = len(row)
            current_boundary = 0
            new_row = [*row]
            for i, char in enumerate(row):
                if char == "#":
                    current_boundary = i + 1
                if char == "O":
                    if new_row[current_boundary] != "O":
                        new_row[current_boundary] = "O"
                        new_row[i] = "."
                    current_boundary += 1
            grid[j] = new_row

        # Reverse the operation at the start of this iteration
        if orientation == "N":
            grid = list(zip(*grid))
        if orientation == "S":
            grid = [row[::-1] for row in grid]
            grid = list(zip(*grid))
        if orientation == "E":
            grid = [row[::-1] for row in grid]

    if iteration_count == CYCLES and (g := grid_to_tuples(grid)) in visited:
        cycles_left = CYCLES - visited[g]
        repetition_after_this_amount_of_cyles = count - visited[g]

        # Overwriting these to only do a few cycles from now on.
        count = 0
        iteration_count = cycles_left % repetition_after_this_amount_of_cyles

    visited[grid_to_tuples(grid)] = count

total = 0
for i, row in enumerate(grid):
    total += row.count("O") * (len(row) - i)
print(f"Part 2: {total}")
