import math

if __name__ == '__main__':
    with open("../input.txt", "r") as input_file:
        time, distance = input_file.read().split("\n")

    times = [int(time) for time in time.split(":")[-1].strip().split(" ") if time]
    distances = [int(dist) for dist in distance.split(":")[-1].strip().split(" ") if dist]

    record_breaking_product = 1
    for index in range(len(times)):
        # Could do binary search here, but the input space is small enough for linear search
        record_breaking_product *= sum(
            (times[index] - hold_for) * hold_for > distances[index]
            for hold_for in range(1, times[index])
        )

    print(f"Total record breaking combinations: {record_breaking_product}")
