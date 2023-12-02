if __name__ == '__main__':
    with open("../input.txt", "r") as input_file:
        power_set_sum = 0
        for line in input_file:
            _, game = line.split(":")
            game_map = dict()

            for revealed in game.split(";"):
                revealed = revealed.split(",")

                for cube_group in revealed:
                    number, colour = cube_group.strip().split(" ")
                    game_map[colour] = max(game_map.get(colour, 0), int(number))

            power_set_sum += game_map["red"] * game_map["green"] * game_map["blue"]

        print(f"The sum of the power sets is: {power_set_sum}")
