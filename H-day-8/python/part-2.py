import numpy as np


def find_cycle_start(start, maps, instructions):
    current_node, instruction_index, total_steps = start, 0, 0

    while current_node[-1] != "Z":
        current_node = maps[current_node][int(data[0][instruction_index] == "R")]
        instruction_index = (instruction_index + 1) % len(instructions)
        total_steps += 1

    return total_steps


if __name__ == '__main__':
    with open("../input.txt", "r") as input_file:
        data = input_file.read().split("\n")

    globe = dict()
    for desert_map in data[2:]:
        from_node, to_nodes = desert_map.split("=")
        globe[from_node.strip()] = [node.strip() for node in to_nodes.replace("(", "").replace(")", "").split(",")]

    cycle_lengths = [find_cycle_start(node, globe, data[0]) for node in globe if node[-1] == "A"]

    # Can't do a simple product, as if cycle lengths share a common factor that will be too large
    steps = np.lcm.reduce(cycle_lengths, dtype="int64")
    print(f"{steps} steps are needed before all end nodes end with Z")
