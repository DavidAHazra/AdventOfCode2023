import collections
import math


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

    parts = []
    current_number, gear_adj = "", set()

    for i in range(h):
        for j in range(w):
            if data[i][j].isdigit():
                current_number += data[i][j]

                for adj_x, adj_y in get_adjacent(i, j, h - 1, w - 1):
                    if data[adj_x][adj_y] == "*":
                        gear_adj.add((adj_x, adj_y))

            else:
                if current_number:
                    parts.append((current_number, gear_adj))

                current_number, gear_adj = "", set()

    gear_nums = collections.defaultdict(list)
    for num, gears in parts:
        for gear in gears:
            gear_nums[gear].append(int(num))

    gear_ratio_sum = sum(
        math.prod(gear_nums[gear])
        for gear in gear_nums
        if len(gear_nums[gear]) == 2
    )

    print(f"The sum of all gear ratios is: {gear_ratio_sum}")
