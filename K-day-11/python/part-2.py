import itertools

EMPTY_FACTOR = 1000000


class StarMap:
    def __init__(self, string_map):
        self.empty_rows = {
            i
            for i in range(len(string_map))
            if all(string_map[i][j] == "." for j in range(len(string_map[0])))
        }

        self.empty_cols = {
            j
            for j in range(len(string_map[0]))
            if all(string_map[i][j] == "." for i in range(len(string_map)))
        }

        self.galaxies = [
            (i, j)
            for i in range(len(string_map))
            for j in range(len(string_map[0]))
            if string_map[i][j] == "#"
        ]

    def get_distance(self, point_a, point_b):
        row_dist = sum(
            EMPTY_FACTOR if row in self.empty_rows else 1
            for row in range(point_a[0], point_b[0], 1 if point_b[0] > point_a[0] else -1)
        )

        col_dist = sum(
            EMPTY_FACTOR if col in self.empty_cols else 1
            for col in range(point_a[1], point_b[1], 1 if point_b[1] > point_a[1] else -1)
        )

        return row_dist + col_dist


if __name__ == '__main__':
    with open("../input.txt", "r") as input_file:
        image = StarMap(input_file.read().splitlines())

    shortest_length_sum = sum(
        image.get_distance(galaxy_a, galaxy_b)
        for galaxy_a, galaxy_b in itertools.combinations(image.galaxies, r=2)
    )

    print(f"The sum of the shortest lengths between all pairs of galaxies is: {shortest_length_sum}")
