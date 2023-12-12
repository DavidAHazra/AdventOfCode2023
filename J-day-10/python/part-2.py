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
        data = input_file.read().splitlines()

    boundary_pipes = {'|', '7', 'F'}
    start_pos = None
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "S":
                start_pos = i, j

    # BFS
    seen = {start_pos}
    queue = deque([start_pos])

    for adj in get_adjacent(data, start_pos):
        if adj == down(start_pos):
            boundary_pipes.add("S")

        queue.append(adj)
        seen.add(adj)

    while queue:
        current = queue.popleft()
        seen.add(current)

        for adj in get_adjacent(data, current):
            if adj not in seen:
                queue.append(adj)

    # For any polygon we can determine if we are inside it by shooting a ray
    # If it crosses the boundary an odd number of times it must be inside the polygon
    enclosed_counter = 0
    for i in range(len(data)):
        boundary_counter = 0
        for j in range(len(data[i])):
            if data[i][j] in boundary_pipes and (i, j) in seen:
                boundary_counter += 1

            if boundary_counter % 2 == 1 and (i, j) not in seen:
                enclosed_counter += 1

    print(f"There are {enclosed_counter} tiles enclosed by the loop")
