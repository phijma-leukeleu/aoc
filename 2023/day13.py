with open("day13_input.txt") as f:
    blocks = f.read().split("\n\n")
    blocks = [[tuple(l) for l in b.splitlines()] for b in blocks]


def find_mirror(block, part):
    # Orientation 0 => vertical mirror
    # Orientation 1 => horizontal mirror
    for orientation, b in enumerate([block, list(zip(*block))]):
        options = []
        for line in b:
            line_options = []
            for i in range(1, len(line)):
                length = min(i, len(line) - i)
                left, right = line[i - length : i], line[i : i + length]
                if left == right[::-1]:
                    line_options.append(i)
            options.append(line_options)

        count_dict = dict()
        for line_options in options:
            for lo in line_options:
                if lo in count_dict:
                    count_dict[lo] += 1
                else:
                    count_dict[lo] = 1

        expected_hits = len(b) - 1 if part == 2 else len(b)
        if expected_hits in count_dict.values():
            indexes = [
                key for key, value in count_dict.items() if value == expected_hits
            ]
            return (0, indexes[0]) if orientation == 1 else (indexes[0], 0)

    raise Exception("This can't happen")


for part in [1, 2]:
    total = 0
    for b in blocks:
        vertical, horizontal = find_mirror(b, part=part)
        total += vertical
        total += horizontal * 100
    print(f"Part {part}: {total}")
