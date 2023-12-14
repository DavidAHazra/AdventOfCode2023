def backtrack(record, groups, start=0):
    if is_a_solution(record, groups):
        return 1

    output = 0
    for i in range(start, len(record)):
        if record[i] == "?":
            for replacement in ".#":
                new_record = record[:i] + replacement + record[i + 1:]
                output += backtrack(new_record, groups, i + 1)

            break

    return output


def is_a_solution(record, groups):
    if "?" in record:
        return False

    split = [len(group) for group in record.split(".") if group]
    return split == groups


if __name__ == '__main__':
    count_sum = 0
    with open("../input.txt", "r") as input_file:
        for line in input_file:
            current_record, record_groups = line.strip().split(" ")
            record_groups = [int(group) for group in record_groups.split(",")]

            count_sum += backtrack(current_record, record_groups)

    print(f"The sum of the counts is: {count_sum}")
