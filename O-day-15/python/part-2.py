def run_hash(step_string):
    current_value = 0
    for char in step_string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256

    return current_value


if __name__ == '__main__':
    boxes = [[] for _ in range(256)]

    with open("../input.txt", "r") as input_file:
        for word in input_file.read().split(","):
            if word[-1] == "-":
                label = word[:-1]
                box = run_hash(label)
                boxes[box] = [lens for lens in boxes[box] if lens[0] != label]

            else:
                label, focal_length = word.split("=")
                box = run_hash(label)

                if not boxes[box]:
                    boxes[box] = [(label, focal_length)]
                    continue

                did_find = False
                for i in range(len(boxes[box])):
                    if boxes[box][i][0] == label:
                        boxes[box][i] = (label, focal_length)
                        did_find = True
                        break

                if not did_find:
                    boxes[box].append((label, focal_length))

    focusing_power = sum(
        (box_number + 1) * (slot_idx + 1) * int(boxes[box_number][slot_idx][1])
        for box_number in range(256)
        for slot_idx in range(len(boxes[box_number]))
    )

    print(f"The focusing power is: {focusing_power}")
