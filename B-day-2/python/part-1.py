if __name__ == '__main__':
    with open("../input.txt", "r") as input_file:
        good_game_sum = 0
        for line in input_file:
            game_id, game = line.split(":")
            game_id, game_map = int(game_id.split(" ")[-1]), dict()

            for revealed in game.split(";"):
                revealed = revealed.split(",")

                for cube_group in revealed:
                    number, colour = cube_group.strip().split(" ")
                    game_map[colour] = max(game_map.get(colour, 0), int(number))

            if game_map["red"] <= 12 and game_map["green"] <= 13 and game_map["blue"] <= 14:
                good_game_sum += game_id

        print(f"The sum of the game IDs of possible games is: {good_game_sum}")
