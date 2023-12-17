from itertools import chain

L = (0, -1)
R = (0, 1)
U = (-1, 0)
D = (1, 0)

MIRROR_DIRECTIONS = {
    "/": {
        R: U, U: R,
        L: D, D: L
    },

    "\\": {
        R: D, D: R,
        L: U, U: L
    },
}


def get_adj(tile, direction, row, col):
    out = []

    if tile == ".":
        out.append(((row + direction[0], col + direction[1]), direction))

    elif tile in "/\\":
        new_dir = MIRROR_DIRECTIONS[tile][direction]

        out.append(((row + new_dir[0], col + new_dir[1]), new_dir))

    elif tile in "-|":
        straight_dirs = {R, L} if tile == '-' else {U, D}
        bend_dirs = {L, R} if tile == '-' else {U, D}

        if direction in straight_dirs:
            out.append(((row + direction[0], col + direction[1]), direction))

        else:
            for bend_dir in bend_dirs:
                out.append(((row + bend_dir[0], col + bend_dir[1]), bend_dir))

    return out


def get_energised(start_pos, start_dir):
    stack = [(start_pos, start_dir)]
    seen = set()

    while stack:
        (i, j), beam_direction = stack.pop()
        seen.add(((i, j), beam_direction))

        for adj_state in get_adj(area[i][j], beam_direction, i, j):
            if 0 <= adj_state[0][0] < len(area) and 0 <= adj_state[0][1] < len(area[0]) and adj_state not in seen:
                stack.append(adj_state)

    return len({pos for pos, _ in seen})


if __name__ == '__main__':
    with open("../input.txt", "r") as input_file:
        area = input_file.read().splitlines()

    rows, cols = len(area), len(area[0])

    states = chain(
        (((i, 0), R) for i in range(rows)),
        (((i, cols - 1), L) for i in range(rows)),
        (((0, j), D) for j in range(cols)),
        (((rows - 1, j), U) for j in range(cols))
    )

    max_energised = max(
        get_energised(start_pos, start_dir)
        for start_pos, start_dir in states
    )

    print(f"The maximum number of energised tiles is: {max_energised}")
