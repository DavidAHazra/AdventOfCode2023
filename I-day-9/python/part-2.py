from collections import deque

if __name__ == '__main__':
    # O(n) / O(n) since the history length is constant

    with open("../input.txt", "r") as input_file:
        histories = [deque(int(val) for val in line.split(" ")) for line in input_file]

    sum_of_extrapolated = 0
    for history in histories:
        process = [history]
        while not all(x == 0 for x in history):
            history = deque(history[i + 1] - history[i] for i in range(len(history) - 1))
            process.append(history)

        process[-1].append(0)
        for i in range(len(process) - 2, -1, -1):
            process[i].appendleft(process[i][0] - process[i + 1][0])

        sum_of_extrapolated += process[0][0]

    print(f"The sum of the extrapolated values is: {sum_of_extrapolated}")
