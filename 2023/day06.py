import re


# Part 1
with open("day6_input.txt") as f:
    lines = f.read().splitlines()

numbers = re.findall(r"\d+", lines[0])
distances = re.findall(r"\d+", lines[1])

total = 1
for t, d in zip(map(int, numbers), map(int, distances)):
    subtotal = 0
    for i in range(t):
        if i * (t - i) > d:
            subtotal += 1
    total *= subtotal

print(total)


# Part 2
t = int("".join(numbers))
d = int("".join(distances))

total = 1
subtotal = 0
for i in range(t):
    if i * (t - i) > d:
        subtotal += 1
total *= subtotal

print(total)
