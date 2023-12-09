if __name__ == '__main__':
    with open("../input.txt", "r") as input_file:
        data = input_file.read().split("\n")

    globe = dict()
    for desert_map in data[2:]:
        from_node, to_nodes = desert_map.split("=")
        globe[from_node.strip()] = [node.strip() for node in to_nodes.replace("(", "").replace(")", "").split(",")]

    current_node, instruction_index, total_steps = "AAA", 0, 0
    while current_node != "ZZZ":
        current_node = globe[current_node][int(data[0][instruction_index] == "R")]
        instruction_index = (instruction_index + 1) % len(data[0])
        total_steps += 1

    print(f"{total_steps} steps are needed to reach ZZZ")

