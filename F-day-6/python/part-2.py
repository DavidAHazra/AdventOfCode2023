import math


if __name__ == '__main__':
    # Read/Process file: O(1) / O(1)
    with open("../input.txt", "r") as input_file:
        time, distance = input_file.read().split("\n")

    time = int(time.split(":")[-1].replace(" ", ""))
    distance = int(distance.split(":")[-1].replace(" ", ""))

    # The distance travelled can be defined as a function f(h) = h * (t - h)
    # h is how long the trigger is held for
    # t is the total time of the game
    # We can solve the equation f(h) = distance for h to find each point on the curve that intersects
    # Then we can subtract these solutions to get the distance between them:

    print(f"There are {math.floor(math.sqrt(time ** 2 - 4 * distance))} ways to beat the record")


