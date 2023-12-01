if __name__ == '__main__':
    calibration_sum = 0
    with open("../input.txt", "r") as input_file:
        for line in input_file:
            # Replace writen numbers in such a way to not disturb any overlapping words
            for value, number in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
                line = line.replace(number, f"{number[0]}{value + 1}{number[-1]}")

            # Part 1 solution
            left, right = 0, len(line) - 1

            while left < right:
                if line[left].isdigit() and line[right].isdigit():
                    break

                if not line[left].isdigit():
                    left += 1

                if not line[right].isdigit():
                    right -= 1

            calibration_sum += 10 * int(line[left]) + int(line[right])

    print(f"The sum of the calibration values is: {calibration_sum}")
