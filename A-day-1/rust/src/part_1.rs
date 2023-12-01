use std::fs::File;
use std::io::{BufRead, BufReader};

pub fn run() {
    let input_file = File::open("../input.txt").expect("Failed to open input.txt");
    let reader = BufReader::new(input_file);
    let mut calibration_sum = 0;

    for line in reader.lines() {
        let line = line.expect("Failed to read line");

        let mut left = 0;
        let mut right = line.len() - 1;

        while left < right {
            let left_char = line.chars().nth(left).unwrap();
            let right_char = line.chars().nth(right).unwrap();

            if left_char.is_digit(10) && right_char.is_digit(10) {
                break;
            }

            if !left_char.is_digit(10) {
                left += 1;
            }

            if !right_char.is_digit(10) {
                right -= 1;
            }
        }

        calibration_sum += 10 * line.chars().nth(left).unwrap().to_digit(10).unwrap()
            + line.chars().nth(right).unwrap().to_digit(10).unwrap();
    }

    println!("The sum of the calibration values is: {}", calibration_sum);
}
