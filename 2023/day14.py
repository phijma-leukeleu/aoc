with open("day14_input.txt") as f:
    grid = f.read().splitlines()

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
print(score)
