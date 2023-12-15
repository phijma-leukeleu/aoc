with open("day15_input.txt") as f:
    strings = f.read().split(",")


def get_score(value):
    retval = 0
    for c in value:
        retval += ord(c)
        retval *= 17
        retval %= 256
    return retval


print(sum(get_score(string) for string in strings))
