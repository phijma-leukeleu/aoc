# Part 1
from utils.vector import Vector2


STEP_VECTOR = {
    "^": Vector2(0, 1),
    ">": Vector2(1, 0),
    "v": Vector2(0, -1),
    "<": Vector2(-1, 0),
}


with open("day03_input.txt") as f:
    steps = list(f.read())


loc = Vector2(0, 0)
visited = {loc}
for step in steps:
    loc += STEP_VECTOR[step]
    visited.add(loc)

print(len(visited))

# Part 2
loc1, loc2 = Vector2(0, 0), Vector2(0, 0)
visited = {loc1, loc2}
steps = iter(steps)
while True:
    try:
        loc1 += STEP_VECTOR[next(steps)]
        loc2 += STEP_VECTOR[next(steps)]
        visited.add(loc1)
        visited.add(loc2)
    except StopIteration:
        break

print(len(visited))
