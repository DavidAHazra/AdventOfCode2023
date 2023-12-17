def find_open_spot_above(board, pos):
    while pos[0] > 0 and board[pos[0] - 1][pos[1]] not in "O#":
        pos = (pos[0] - 1, pos[1])

    return pos


def move_spheres_north(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "O":
                new_spot = find_open_spot_above(board, (i, j))
                board[i][j] = "."
                board[new_spot[0]][new_spot[1]] = "O"

    return board


if __name__ == '__main__':
    with open("../input.txt", "r") as input_file:
        dish = [list(line.strip()) for line in input_file.read().splitlines()]

    dish = move_spheres_north(dish)

    total_load = sum(
        row.count("O") * (len(dish) - index)
        for index, row in enumerate(dish)
    )

    print(f"The total load on the northern beams is: {total_load}")
