from itertools import combinations
import math


# Part 1
with open("day02_input.txt") as f:
    boxes = f.read().splitlines()

boxes = [sorted(map(int, b.split("x"))) for b in boxes]

print(sum([b[0] * b[1] + 2 * sum(map(math.prod, combinations(b, 2))) for b in boxes]))


# Part 2
print(sum([2 * b[0] + 2 * b[1] + math.prod(b) for b in boxes]))
