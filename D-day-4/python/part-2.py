import collections

if __name__ == '__main__':
    with open("../input.txt", "r") as input_file:
        cards = dict()
        for line in input_file:
            card_num, data = line.split(":")
            card_num = int(card_num.replace("Card", ""))

            winning, played = data.split("|")
            winning = set(int(num) for num in winning.split(" ") if num)
            played = [int(num) for num in played.split(" ") if num]

            cards[card_num] = (winning, played)

        holding = collections.defaultdict(lambda: 1)
        for card_num in range(1, len(cards) + 1):
            num_wins = sum(played_number in cards[card_num][0] for played_number in cards[card_num][1])
            for update in range(card_num + 1, min(len(cards), card_num + num_wins + 1)):
                holding[update] += holding[card_num]

        # Can't use sum(holding.values()) as some numbers may not be initialised in the defaultdict
        holding_sum = sum(holding[card_num] for card_num in range(1, len(cards) + 1))
        print(f"You end up with {holding_sum} scratchcards")
