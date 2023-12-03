import math


# Part 1
def is_valid(data):
    color_dict = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    for set_of_cubes in data.split("; "):
        for cubes in set_of_cubes.split(", "):
            count, color = cubes.split()
            if color_dict[color] - int(count) < 0:
                return False
    return True


total = 0

with open("day2_input.txt") as f:
    lines = f.readlines()

for i, line in enumerate(lines, start=1):
    _, game_data = line.split(":")
    if is_valid(game_data):
        total += i

print(total)


# Part 2
def get_power(data):
    color_dict = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for set_of_cubes in data.split("; "):
        for cubes in set_of_cubes.split(", "):
            count, color = cubes.split()
            color_dict[color] = max(color_dict[color], int(count))
    return math.prod(color_dict.values())


total = 0

with open("day2_input.txt") as f:
    lines = f.readlines()

for line in lines:
    _, game_data = line.split(":")
    total += get_power(game_data)

print(total)
