import hashlib

with open("day04_input.txt") as f:
    key = f.read()

# Part 1 + 2
for part in ["00000", "000000"]:
    i = 0
    while True:
        string = f"{key}{i}"
        if hashlib.md5(bytes(string, "utf-8")).hexdigest().startswith(part):
            print(i)
            break
        i += 1
