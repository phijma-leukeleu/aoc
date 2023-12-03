import math

# Quick and dirty

with open("day3_input.txt") as f:
    grid = f.read().splitlines()

symbol_part_numbers = dict()
for i, row in enumerate(grid):
    number = ""
    symbol = None
    for j, cell in enumerate(row):
        if cell.isdigit():
            number += cell
            if not symbol:
                for dj in [-1, 0, 1]:
                    for di in [-1, 0, 1]:
                        try:
                            cell_adjacent = grid[i + di][j + dj]
                        except IndexError:
                            continue

                        if cell_adjacent != "." and not cell_adjacent.isdigit():
                            symbol = cell_adjacent, i + di, j + dj
        else:
            if symbol:
                symbol_part_numbers.setdefault(symbol, []).append(int(number))
            number = ""
            symbol = None

    if symbol:
        symbol_part_numbers.setdefault(symbol, []).append(int(number))

# Part1
print(sum(sum(value) for value in symbol_part_numbers.values()))

# Part2
print(
    sum(
        math.prod(value)
        for key, value in symbol_part_numbers.items()
        if key[0] == "*" and len(value) == 2
    )
)
