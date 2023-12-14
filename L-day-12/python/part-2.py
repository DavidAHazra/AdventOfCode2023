from functools import cache


def solve_problem(record, groups):
    # Hard one :(

    # Add . at the end to make EOL cleaner for group scanning
    record += "."

    @cache
    def count_solutions(position, group_index):
        # Base case: end of input
        if position >= len(record):
            return 1 if group_index == len(groups) else 0

        total_count = 0

        # Case 1: Treat this character (either . or ?) as a .
        if record[position] in '.?':
            total_count += count_solutions(position + 1, group_index)

        # Case 2: Treat this character (either # or ?) as a #
        # Move to next group iff it's valid
        if record[position] in '#?' and group_index < len(groups):
            end_of_group = position + groups[group_index]

            if end_of_group <= len(record):
                valid_group = "." not in record[position: end_of_group]

                if valid_group and record[end_of_group] != '#':
                    total_count += count_solutions(end_of_group + 1, group_index + 1)

        return total_count

    return count_solutions(0, 0)


if __name__ == '__main__':
    count_sum = 0
    with open("../input.txt", "r") as input_file:
        for line in input_file:
            current_record, record_groups = line.strip().split(" ")
            record_groups = [int(group) for group in record_groups.split(",")]

            count_sum += solve_problem("?".join([current_record] * 5), record_groups * 5)

    print(f"The sum of the counts is: {count_sum}")
