import functools


# Part 1
with open("day07_input.txt") as f:
    lines = f.read().splitlines()


CARDS = list("AKQJT98765432")


def get_score(cards):
    scores = dict()
    for card in cards:
        if card in scores:
            scores[card] += 1
        else:
            scores[card] = 1

    counts = list(scores.values())

    if 5 in counts:
        return 7
    elif 4 in counts:
        return 6
    elif 3 in counts and 2 in counts:
        return 5
    elif 3 in counts:
        return 4
    elif counts.count(2) == 2:
        return 3
    elif 2 in counts:
        return 2
    else:
        return 1


def compare_hands(hand1, hand2):
    h1, h2 = hand1.split()[0], hand2.split()[0]
    s1, s2 = get_score(h1), get_score(h2)

    if s1 != s2:
        return s1 - s2

    for c1, c2 in zip(h1, h2):
        if difference := CARDS.index(c2) - CARDS.index(c1):
            return difference


print(
    sum(
        i * int(hand.split(" ")[1])
        for i, hand in enumerate(
            sorted(lines, key=functools.cmp_to_key(compare_hands)), start=1
        )
    )
)


# Part 2
CARDS = list("AKQT98765432J")


def get_score_part2(cards):
    j_count = cards.count("J")

    if j_count == 5:
        return 7

    cards_without_js = cards.replace("J", "")

    return max(
        get_score(cards_without_js + option * j_count)  # Use `get_score` from part 1
        for option in set(cards_without_js)
    )


def compare_hands_part2(hand1, hand2):
    h1, h2 = hand1.split()[0], hand2.split()[0]
    s1, s2 = get_score_part2(h1), get_score_part2(h2)

    if s1 != s2:
        return s1 - s2

    for c1, c2 in zip(h1, h2):
        if difference := CARDS.index(c2) - CARDS.index(c1):
            return difference


print(
    sum(
        i * int(hand.split(" ")[1])
        for i, hand in enumerate(
            sorted(lines, key=functools.cmp_to_key(compare_hands_part2)),
            start=1,
        )
    )
)
