with open("day18_input.txt") as f:
    instructions = f.read().splitlines()

DIRS = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, -1),
    "D": (0, 1),
}

start = (0, 0)
loop = {start}
pos = start

for i in instructions:
    d, l, _ = i.split()
    for _ in range(int(l)):
        x, y = pos
        dx, dy = DIRS[d]
        pos = x + dx, y + dy
        loop.add(pos)

to_check = [(1, 1)]  # It's magic ✨
while to_check:
    x, y = to_check.pop()
    right = x + 1, y
    left = x - 1, y
    up = x, y - 1
    down = x, y + 1
    for p in [up, down, left, right]:
        if p not in loop:
            loop.add(p)
            to_check.append(p)
print(len(loop))
