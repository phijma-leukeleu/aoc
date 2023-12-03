import re

# Part 1
total = 0

with open("day1_input.txt") as f:
    lines = f.readlines()

for line in lines:
    numbers = re.findall(r"[0-9]", line)
    total += int(numbers[0] + numbers[-1])

print(total)


# Part 2
WORD_NUMBER_MAPPING = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

total = 0

with open("day1_input.txt") as f:
    lines = f.readlines()

for line in lines:
    numbers = re.findall(f"(?=([0-9]|{'|'.join(WORD_NUMBER_MAPPING.keys())}))", line)
    number1 = WORD_NUMBER_MAPPING.get(numbers[0], numbers[0])
    number2 = WORD_NUMBER_MAPPING.get(numbers[-1], numbers[-1])
    total += int(number1 + number2)

print(total)
