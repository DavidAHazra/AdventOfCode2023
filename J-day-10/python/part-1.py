from collections import deque


def right(position):
    return position[0], position[1] + 1


def left(position):
    return position[0], position[1] - 1


def up(position):
    return position[0] - 1, position[1]


def down(position):
    return position[0] + 1, position[1]


def in_bounds(p, i_len, j_len):
    return 0 <= p[0] < i_len and 0 <= p[1] < j_len


def in_bounds_helper(i_len, j_len):
    def helper(p):
        return in_bounds(p, i_len, j_len)

    return helper


def get_adjacent(mapp, pos):
    pipe = mapp[pos[0]][pos[1]]

    if pipe == ".":
        return []

    if pipe == "-":
        return filter(in_bounds_helper(len(mapp), len(mapp[0])), [left(pos), right(pos)])

    if pipe == "|":
        return filter(in_bounds_helper(len(mapp), len(mapp[0])), [up(pos), down(pos)])

    if pipe == "F":
        return filter(in_bounds_helper(len(mapp), len(mapp[0])), [right(pos), down(pos)])

    if pipe == "7":
        return filter(in_bounds_helper(len(mapp), len(mapp[0])), [left(pos), down(pos)])

    if pipe == "J":
        return filter(in_bounds_helper(len(mapp), len(mapp[0])), [up(pos), left(pos)])

    if pipe == "L":
        return filter(in_bounds_helper(len(mapp), len(mapp[0])), [right(pos), up(pos)])

    if pipe == "S":
        s_valid = []

        u, l, r, d = up(pos), left(pos), right(pos), down(pos)

        if in_bounds(u, len(mapp), len(mapp[0])) and mapp[u[0]][u[1]] in "|F7":
            s_valid.append(u)

        if in_bounds(l, len(mapp), len(mapp[0])) and mapp[l[0]][l[1]] in "-FL":
            s_valid.append(l)

        if in_bounds(r, len(mapp), len(mapp[0])) and mapp[r[0]][r[1]] in "-7J":
            s_valid.append(r)

        if in_bounds(d, len(mapp), len(mapp[0])) and mapp[d[0]][d[1]] in "|LJ":
            s_valid.append(d)

        return s_valid


if __name__ == '__main__':
    # TODO: make this whole program less ugly

    with open("../input.txt", "r") as input_file:
        data = [line.strip() for line in input_file]

    start_pos = None
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "S":
                start_pos = (i, j)

    # Do BFS to get distance
    seen = {start_pos}
    queue = deque([(start_pos, 0)])
    max_depth = 0
    while queue:
        current, depth = queue.popleft()

        seen.add(current)
        max_depth = max(max_depth, depth)

        for adj in get_adjacent(data, current):
            if adj not in seen:
                queue.append((adj, depth + 1))

    print(f"The farthest point from the start of the loop is: {max_depth}")
