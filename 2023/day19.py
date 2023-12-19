import re

with open("day19_input.txt") as f:
    routes, things = f.read().split("\n\n")


routes_dict = {}
for route in routes.splitlines():
    name, options = route[:-1].split("{")
    options = options.split(",")
    for o in options:
        routes_dict.setdefault(name, []).append(o.split(":") if ":" in o else o)

total = 0
for t in things.splitlines():
    loc = "in"
    x, m, a, s = [int(x) for x in re.findall(r"\d+", t)]
    while loc not in ["A", "R"]:
        for o in routes_dict[loc]:
            if isinstance(o, list) and eval(o[0]):
                loc = o[1]
                break
            else:
                loc = o
    if loc == "A":
        total += x + m + a + s

print(f"Part 1: {total}")
