with open("day01_input.txt") as f:
    movements = list(f.read())

# Part 1
print(movements.count("(") - movements.count(")"))

# Part 2
pos = 0
for i, movement in enumerate(movements, start=1):
    if movement == "(":
        pos += 1
    else:
        pos -= 1

    if pos == -1:
        break

print(pos)
