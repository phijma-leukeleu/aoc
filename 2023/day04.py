def get_card_score(card):
    _, parts = card.split(":")
    winning_numbers, my_numbers = parts.split("|")
    return len(set(winning_numbers.split()) & set(my_numbers.split()))


# Part 1
total = 0

with open("day4_input.txt") as f:
    scratchcards = f.read().splitlines()

for card in scratchcards:
    if score := get_card_score(card):
        total += 2 ** (score - 1)

print(total)


# Part 2
with open("day4_input.txt") as f:
    scratchcards = f.read().splitlines()

scratchcard_counts = [1] * len(scratchcards)

for card_number, card in enumerate(scratchcards):
    score = get_card_score(card)
    for s in range(card_number + 1, card_number + 1 + score):
        scratchcard_counts[s] += scratchcard_counts[card_number]

print(sum(scratchcard_counts))
