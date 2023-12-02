use std::cmp;
use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn binary_split(input: &str, split_char: char) -> (&str, &str) {
    let mut split = input.split(split_char);
    let first = split.next().expect("Failed to get first half");
    let second = split.next().expect("Failed to get second half");

    (first, second)
}

pub fn run() {
    let input_file = File::open("../input.txt").expect("Failed to open input.txt");
    let reader = BufReader::new(input_file);
    let mut power_set_sum: u16 = 0;

    for line in reader.lines() {
        let line = line.expect("Failed to read line");

        let (_, game) = binary_split(&line, ':');
        let mut game_map: HashMap<&str, u16> = HashMap::new();

        for revealed in game.split(";") {
            for cube_group in revealed.split(",") {
                let (number, colour) = binary_split(&(cube_group.trim()), ' ');
                let number = number
                    .trim()
                    .parse::<u16>()
                    .expect("Failed to parse number");

                let current_value = *game_map.entry(colour).or_insert(0);
                game_map.insert(colour, cmp::max(current_value, number));
            }
        }

        power_set_sum += *game_map.get("red").unwrap() * *game_map.get("green").unwrap()
            * *game_map.get("blue").unwrap();
    }

    println!("The sum of the power sets is: {}", power_set_sum);
}
