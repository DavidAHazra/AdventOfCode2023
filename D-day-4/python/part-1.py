if __name__ == '__main__':
    with open("../input.txt", "r") as input_file:
        total_score = 0
        for line in input_file:
            _, data = line.split(":")
            winning, played = data.split("|")
            winning = set(int(num) for num in winning.split(" ") if num)
            played = [int(num) for num in played.split(" ") if num]

            num_won = sum(played_number in winning for played_number in played)

            if num_won > 0:
                total_score += 2 ** (num_won - 1)

        print(f"The total score from all scratch cards is: {total_score}")

