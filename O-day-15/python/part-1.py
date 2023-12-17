def run_hash(step_string):
    current_value = 0
    for char in step_string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256

    return current_value


if __name__ == '__main__':
    with open("../input.txt", "r") as input_file:
        result_sum = sum(
            run_hash(word)
            for word in input_file.read().split(",")
        )

    print(f"The sum of the results is: {result_sum}")
