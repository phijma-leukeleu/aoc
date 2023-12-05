# Part 1
with open("day5_input.txt") as f:
    seeds, *maps = f.read().split("\n\n")

seeds = list(map(int, seeds.split(":")[1].split()))

for m in maps:
    _, *parts = m.splitlines()
    parts = [list(map(int, r.split())) for r in parts]
    for i, seed in enumerate(seeds):
        for p in parts:
            if p[1] <= seed < p[1] + p[2]:
                seeds[i] -= p[1] - p[0]

print(min(seeds))

# Part 2
# 😭
