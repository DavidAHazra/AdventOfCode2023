import collections
from functools import cmp_to_key, cache

CARD_ORDER = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


@cache
def get_type(current):
    counts = list(collections.Counter(current).values())

    if 5 in counts:
        # 5 of a kind
        return 1

    if 4 in counts:
        # 4 of a kind
        return 2

    if 3 in counts:
        if 2 in counts:
            # Full house
            return 3

        # 3 of a kind
        return 4

    if counts.count(2) == 2:
        # Two pair
        return 5

    if 2 in counts:
        # Pair
        return 6

    # High card
    return 7


@cmp_to_key
def compare_hands(hand_a, hand_b):
    type_a, type_b = get_type(hand_a), get_type(hand_b)

    if type_a < type_b:
        return -1

    if type_b < type_a:
        return 1

    for card_a, card_b in zip(hand_a, hand_b):
        card_a, card_b = CARD_ORDER.index(card_a), CARD_ORDER.index(card_b)

        if card_a < card_b:
            return -1

        if card_b < card_a:
            return 1

    return 0


if __name__ == '__main__':
    hands, bid_map = list(), dict()
    with open("../input.txt", "r") as input_file:
        for line in input_file:
            hand, bid = line.split(" ")
            bid_map[hand] = int(bid)
            hands.append(hand)

    total_winnings = sum(
        bid_map[hand] * (len(hands) - index)
        for index, hand in enumerate(sorted(hands, key=compare_hands))
    )

    print(f"The total winnings are: {total_winnings}")
