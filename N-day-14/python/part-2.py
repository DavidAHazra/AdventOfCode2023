import numpy as np


TARGET_END = 1000000000


def find_open_spot_above(board, pos):
    while pos[0] > 0 and board[pos[0] - 1, pos[1]] not in "O#":
        pos = (pos[0] - 1, pos[1])
    return pos


def move_spheres_north(board):
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if board[i, j] == "O":
                new_spot = find_open_spot_above(board, (i, j))
                board[i, j] = "."
                board[new_spot] = "O"

    return board


def cycle(board):
    for _ in range(4):
        board = move_spheres_north(board)
        board = np.rot90(board, k=-1)

    return board


def cycle_until_repeat(board):
    seen_states = {}
    for i in range(TARGET_END):
        board_hash = hash(board.tobytes())
        if board_hash in seen_states:
            return i, seen_states[board_hash], board

        seen_states[board_hash] = i
        board = cycle(board)

    return None, None, board


if __name__ == '__main__':
    with open("../input.txt", "r") as input_file:
        dish = np.array([list(line.strip()) for line in input_file.readlines()])

    cycle_count, cycle_start, final_state = cycle_until_repeat(dish)
    assert cycle_count is not None

    # The 1 billionth state is somewhere in the cycle
    # Start at the beginning and run the process for the remaining distance
    cycle_length = cycle_count - cycle_start
    remaining_cycles = (TARGET_END - cycle_start) % cycle_length
    for _ in range(remaining_cycles):
        final_state = cycle(final_state)

    final_load = sum(
        (row == "O").sum() * (final_state.shape[0] - index)
        for index, row in enumerate(final_state)
    )

    print(f"Load after {TARGET_END} cycles: {final_load}")
