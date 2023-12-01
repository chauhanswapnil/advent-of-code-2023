use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};

pub fn day_01() {
    part_1();
    part_2();
}

fn part_2() {
    let lines = read_file("../inputs/day_01_part2.txt");
    let number_map: HashMap<&str, &str> = [
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
    ]
    .iter()
    .cloned()
    .collect();

    let mut sum = 0;

    for line in lines {
        let mut got_first = false;
        let mut last_digit_str = String::new();
        let mut number_string = String::new();
        for (index, character) in line.char_indices() {
            if character.is_ascii_digit() {
                if !got_first {
                    number_string = number_string + &character.to_string();
                    got_first = true;
                }
                last_digit_str = character.to_string();
            }

            // This gets the number word
            if let Some(substring) = line.get(index..) {
                for (word, number) in &number_map {
                    if substring.starts_with(word) {
                        if !got_first {
                            // println!("Matched Number {}", number.to_string());
                            number_string = number_string + &number.to_string();
                            got_first = true;
                        }
                        last_digit_str = number.to_string();
                    }
                }
            }
        }
        number_string = number_string + &last_digit_str;
        // println!("Number is {}", number_string);
        sum = sum + number_string.parse::<u32>().unwrap();
    }
    println!("Sum is {}", sum);
}

fn part_1() {
    let lines = read_file("../inputs/day_01_part1.txt");
    let mut sum = 0;
    for line in lines {
        let mut got_first = false;
        let mut last_digit_str = String::new();
        let mut number_string = String::new();
        for character in line.chars() {
            if character.is_ascii_digit() {
                if !got_first {
                    number_string = number_string + &character.to_string();
                    got_first = true;
                }
                last_digit_str = character.to_string();
            }
        }
        number_string = number_string + &last_digit_str;
        sum = sum + number_string.parse::<u32>().unwrap();
    }
    println!("Sum is {}", sum);
}

fn read_file(filepath: &str) -> Vec<String> {
    let file = File::open(filepath).unwrap();
    let reader = BufReader::new(file);
    let mut lines = Vec::new();
    for line in reader.lines() {
        lines.push(line.unwrap());
    }
    return lines;
}
