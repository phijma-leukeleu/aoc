from itertools import pairwise

with open("day05_input.txt") as file:
    words = file.read().splitlines()


# Part 1
VOWELS = "aeiou"
FORBIDDEN = ["ab", "cd", "pq", "xy"]
TWICE = [c + c for c in "abcdefghijklmnopqrstuvwxyz"]


def is_nice_part1(value):
    if any(f in value for f in FORBIDDEN):
        return False
    if sum(value.count(v) for v in VOWELS) < 3:
        return False
    if not any(t in value for t in TWICE):
        return False
    return True


print(sum(1 for word in words if is_nice_part1(word)))


# Part 2
def is_nice_part2(value):
    has_pair = any(value.count("".join(pair)) > 1 for pair in pairwise(value))
    has_triplet = any(c1 + c2 + c1 in value for c1 in set(value) for c2 in set(value))
    return has_pair and has_triplet


print(sum(1 for word in words if is_nice_part2(word)))
