def get_adjacent(x, y, max_x, max_y):
    return {
        (max(0, min(max_x, x + dx)), max(0, min(max_y, y + dy)))
        for dx in range(-1, 2)
        for dy in range(-1, 2)
    }


if __name__ == '__main__':
    with open("../input.txt", "r") as input_file:
        data = [line.strip() for line in input_file.readlines()]

    h, w = len(data), len(data[0])

    part_sum = 0
    current_number, is_part = "", False

    for i in range(h):
        for j in range(w):
            if data[i][j].isdigit():
                current_number += data[i][j]

                for adj_x, adj_y in get_adjacent(i, j, h - 1, w - 1):
                    if data[adj_x][adj_y] != "." and not data[adj_x][adj_y].isdigit():
                        is_part = True
                        break

            else:
                if current_number and is_part:
                    part_sum += int(current_number)

                current_number, is_part = "", False

    print(f"The sum of all part numbers is: {part_sum}")


