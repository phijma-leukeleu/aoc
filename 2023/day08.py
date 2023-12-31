import math


def get_step_count(current):
    step_count = 0
    while True:
        for d in dirs:
            step_count += 1
            current = locs[current][d]
            if current.endswith("Z"):
                return step_count


# Part 1
with open("day08_input.txt") as f:
    dirs_input, locs_input = f.read().split("\n\n")
    locs_input = locs_input.splitlines()

dirs = list(dirs_input)
locs = dict()
for loc in locs_input:
    l, i = loc.split(" = ")
    left, right = i[1:-1].split(", ")
    locs[l] = {
        "L": left,
        "R": right,
    }

print(get_step_count("AAA"))


# Part 2
start_locations = [k for k in locs.keys() if k.endswith("A")]

print(math.lcm(*map(get_step_count, start_locations)))
