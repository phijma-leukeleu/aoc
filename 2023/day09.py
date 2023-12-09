from itertools import pairwise


with open("day09_input.txt") as f:
    sequences = f.read().splitlines()

sequences = [[int(seq) for seq in sequence.split()] for sequence in sequences]

# Part 1 + 2
for part in [1, 2]:
    total = 0
    for seq in sequences:
        results = [seq]

        while not all(s == 0 for s in results[-1]):
            results.append([s[1] - s[0] for s in pairwise(results[-1])])

        if part == 1:
            total += sum(s[-1] for s in results)
        elif part == 2:
            total += sum(s[0] if i % 2 == 0 else -s[0] for i, s in enumerate(results))

    print(f"Part {part}: {total}")
