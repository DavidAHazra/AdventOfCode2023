# AdventOfCode2023

This is my attempt at [Advent of Code 2023](https://adventofcode.com/2023/about).

Also included is my estimation of the time complexity (Time / Space). As is standard, if the input needs to be saved
to a variable in some way that does not affect the Space complexity.

For those days where I have not yet completed both parts, I will not be pushing my solutions
(to give me time to work on them :)).

These solutions work on my input, but they're not tested rigorously so please feel free to try them out and open a PR to fix any issues.

This year I'm learning Rust, so I'll *try* provide solutions in Python *and* Rust. This may not always be done immediately :).

## Advent Progress

| Advent Stage |                                         Python Solution                                         |                                          Rust Solution                                           |                  Time                   | Space |
|:------------:|:-----------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------:|:---------------------------------------:|:-----:|
|    Day 1     | [Part 1](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/A-day-1/python/part-1.py)  | [Part 1](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/A-day-1/rust/src/part_1.rs) |                  O(n)                   | O(1)  |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/A-day-1/python/part-2.py)  | [Part 2](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/A-day-1/rust/src/part_2.rs) |                  O(n)                   | O(1)  |
|    Day 2     | [Part 1](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/B-day-2/python/part-1.py)  | [Part 1](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/B-day-2/rust/src/part_1.rs) |                  O(n)                   | O(1)  |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/B-day-2/python/part-2.py)  | [Part 2](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/B-day-2/rust/src/part_2.rs) |                  O(n)                   | O(1)  |
|    Day 3     | [Part 1](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/C-day-3/python/part-1.py)  |                                                                                                  |                  O(hw)                  | O(1)  |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/C-day-3/python/part-2.py)  |                                                                                                  |                  O(hw)                  | O(hw) |
|    Day 4     | [Part 1](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/D-day-4/python/part-1.py)  |                                                                                                  |                  O(n)                   | O(n)  |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/D-day-4/python/part-2.py)  |                                                                                                  |                O($n^2$)                 | O(n)  |
|    Day 5     | [Part 1](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/E-day-5/python/part-1.py)  |                                                                                                  |                  O(n)                   | O(n)  |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/E-day-5/python/part-2.py)  |                                                                                                  |                  O(n)                   | O(n)  |
|    Day 6     | [Part 1](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/F-day-6/python/part-1.py)  |                                                                                                  |          O($n \times T_{max}$)          | O(n)  |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/F-day-6/python/part-2.py)  |                                                                                                  |                  O(1)                   | O(1)  |
|    Day 7     | [Part 1](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/G-day-7/python/part-1.py)  |                                                                                                  |               O(n log n)                | O(n)  |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/G-day-7/python/part-2.py)  |                                                                                                  |               O(n log n)                | O(n)  |
|    Day 8     | [Part 1](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/H-day-8/python/part-1.py)  |                                                                                                  |           O($n + V \times I$)           | O(n)  |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/H-day-8/python/part-2.py)  |                                                                                                  |           O($n + V \times I$)           | O(n)  |
|    Day 9     | [Part 1](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/I-day-9/python/part-1.py)  |                                                                                                  |                  O(n)                   | O(n)  |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/I-day-9/python/part-2.py)  |                                                                                                  |                  O(n)                   | O(n)  |
|    Day 10    | [Part 1](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/J-day-10/python/part-1.py) |                                                                                                  |                  O(hw)                  | O(hw) |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/J-day-10/python/part-2.py) |                                                                                                  |                  O(hw)                  | O(hw) |
|    Day 11    | [Part 1](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/K-day-11/python/part-1.py) |                                                                                                  | O($h^2 \times w^2 \times \max (h, w) $) | O(hw) |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/K-day-11/python/part-2.py) |                                                                                                  |                  O(hw)                  | O(hw) |
|    Day 12    | [Part 1](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/L-day-12/python/part-1.py) |                                                                                                  |                O($2^n$)                 | O(n)  |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/L-day-12/python/part-2.py) |                                                                                                  |                  O(n)                   | O(n)  |
|    Day 13    | [Part 1](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/M-day-13/python/part-1.py) |                                                                                                  |                O($n^2$)                 | O(n)  |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/M-day-13/python/part-2.py) |                                                                                                  |                O($n^2$)                 | O(n)  |
|    Day 14    | [Part 1](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/N-day-14/python/part-1.py) |                                                                                                  |                O($h^2w$)                | O(hw) |
|              | [Part 2](https://github.com/DavidAHazra/AdventOfCode2023/blob/master/N-day-14/python/part-2.py) |                                                                                                  |                O($h^2w$)                | O(hw) |
