from collections import Counter
from functools import reduce


def read_file(file_path: str):
    with open(file_path, 'r') as file:
        return file.readlines()


def read_file_as_string(file_path: str):
    with open(file_path, 'r') as file:
        return file.read()


def hand_category(cards):
    label_counts = {label: cards.count(label) for label in set(cards)}
    sorted_counts = sorted(label_counts.values(), reverse=True)

    if sorted_counts == [5]:
        return "Five of a kind"
    elif sorted_counts == [4, 1]:
        return "Four of a kind"
    elif sorted_counts == [3, 2]:
        return "Full house"
    elif sorted_counts == [3, 1, 1]:
        return "Three of a kind"
    elif sorted_counts == [2, 2, 1]:
        return "Two pair"
    elif sorted_counts == [2, 1, 1, 1]:
        return "One pair"
    else:
        return "High card"


def get_card_value(card):
    if card.isdigit():
        return int(card)
    elif card == 'A':
        return 14
    elif card == 'K':
        return 13
    elif card == 'Q':
        return 12
    elif card == 'J':
        return 11
    elif card == 'T':
        return 10
    else:
        raise Exception("Should not happen!")


def hand_value(hand):
    return [get_card_value(card) for card in hand]


categories = [
    "High card",
    "One pair",
    "Two pair",
    "Three of a kind",
    "Full house",
    "Four of a kind",
    "Five of a kind",
]


def part_1():
    inputs = read_file_as_string("../inputs/day_07.txt")
    hands_bids = [(line.split()[0], int(line.split()[1])) for line in inputs.split('\n')]
    sorted_hands_bids = sorted(
        hands_bids,
        key=lambda x: (categories.index(hand_category(x[0])), hand_value(x[0])),
    )
    for hand in sorted_hands_bids:
        print(hand)
    print(sum(t[1] * (i + 1) for i, t in enumerate(sorted_hands_bids)))


def hand_category_2(cards):
    label_counts = {label: cards.count(label) for label in set(cards)}

    if 'J' in label_counts and label_counts['J'] != 5:
        non_j_labels = [label for label in label_counts if label != 'J']
        max_label = max(non_j_labels, key=label_counts.get)
        label_counts[max_label] += label_counts['J']
        label_counts.pop('J')

    sorted_counts = sorted(label_counts.values(), reverse=True)

    if sorted_counts == [5] or sorted_counts == [5, 0]:
        return "Five of a kind"
    elif sorted_counts == [4, 1] or sorted_counts == [4, 1, 0]:
        return "Four of a kind"
    elif sorted_counts == [3, 2] or sorted_counts == [3, 2, 0]:
        return "Full house"
    elif sorted_counts == [3, 1, 1] or sorted_counts == [3, 1, 1, 0]:
        return "Three of a kind"
    elif sorted_counts == [2, 2, 1] or sorted_counts == [2, 2, 2, 0]:
        return "Two pair"
    elif sorted_counts == [2, 1, 1, 1] or sorted_counts == [2, 1, 1, 1, 0]:
        return "One pair"
    else:
        return "High card"


def get_card_value_2(card):
    if card.isdigit():
        return int(card)
    elif card == 'A':
        return 14
    elif card == 'K':
        return 13
    elif card == 'Q':
        return 12
    elif card == 'T':
        return 10
    elif card == 'J':  # J is not joker
        return 1
    else:
        raise Exception("Should not happen!")


def hand_value_2(hand):
    return [get_card_value_2(card) for card in hand]


categories_2 = [
    "High card",
    "One pair",
    "Two pair",
    "Three of a kind",
    "Full house",
    "Four of a kind",
    "Five of a kind",
]


def part_2():
    inputs = read_file_as_string("../inputs/day_07.txt")
    hands_bids = [(line.split()[0], int(line.split()[1])) for line in inputs.split('\n')]
    for hand, bid in hands_bids:
        print(f"{hand} is {hand_category_2(hand)}")
    sorted_hands_bids = sorted(
        hands_bids,
        key=lambda x: (categories_2.index(hand_category_2(x[0])), hand_value_2(x[0])),
    )
    for hand, bids in sorted_hands_bids:
        print(f"{hand} is {hand_category_2(hand)}")
    print(sum(t[1] * (i + 1) for i, t in enumerate(sorted_hands_bids)))


if __name__ == "__main__":
    part_1()
    part_2()
