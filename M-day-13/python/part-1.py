import numpy as np


def lines_above_mirror(pattern):
    for i in range(pattern.shape[0] - 1):
        above_lines = pattern[:i + 1, :]
        below_lines = pattern[i + 1:, :]

        max_len = min(above_lines.shape[0], below_lines.shape[0])
        differences = (above_lines[::-1][:max_len] != below_lines[:max_len]).sum()

        if differences == 0:
            return i + 1


if __name__ == '__main__':
    note_summary_sum = 0
    with open("../input.txt", "r") as input_file:
        for notes in input_file.read().split("\n\n"):
            notes = np.array([list(line) for line in notes.splitlines()])

            above_mirror = lines_above_mirror(notes)

            if above_mirror is not None:
                note_summary_sum += 100 * above_mirror

            else:
                note_summary_sum += lines_above_mirror(notes.T)

    print(f"The sum of the note summaries is: {note_summary_sum}")
