import re

with open("day06_input.txt") as file:
    instructions = file.read().splitlines()

lights_on = set()

for instruction in instructions:
    x1, y1, x2, y2 = map(int, re.findall(r"\d+", instruction))
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if "on" in instruction:
                lights_on.add((i, j))
            elif "off" in instruction:
                lights_on.discard((i, j))
            elif (i, j) in lights_on:
                lights_on.remove((i, j))
            else:
                lights_on.add((i, j))

print(len(lights_on))


# Part 2
lights = [[0 for _ in range(1000)] for _ in range(1000)]

for instruction in instructions:
    x1, y1, x2, y2 = map(int, re.findall(r"\d+", instruction))

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if "on" in instruction:
                lights[i][j] += 1
            elif "off" in instruction:
                lights[i][j] = max(0, lights[i][j] - 1)
            else:  # toggle
                lights[i][j] += 2

print(sum([sum(row) for row in lights]))
