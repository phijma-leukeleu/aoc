with open("day15_input.txt") as f:
    strings = f.read().split(",")


# Part 1
def get_score(value):
    retval = 0
    for c in value:
        retval += ord(c)
        retval *= 17
        retval %= 256
    return retval


print(f"Part 1: {sum(get_score(string) for string in strings)}")


# Part 2
boxes = [dict() for _ in range(256)]

for string in strings:
    if string.endswith("-"):
        label = string.replace("-", "")
        i = get_score(label)
        if label in boxes[i]:
            del boxes[i][label]
    else:
        label, _, focal = string.partition("=")
        i = get_score(label)
        boxes[i][label] = int(focal)

focusing_power = 0
for i, box in enumerate(boxes, start=1):
    for j, label in enumerate(box, start=1):
        focusing_power += i * j * box[label]

print(f"Part 2: {focusing_power}")
