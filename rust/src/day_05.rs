use std::io::BufRead;
use crate::utils::read_file;

pub fn day_05() {
    let lines_part_1 = read_file("../inputs/day_05.txt");
    println!("Day 05 - Part - 1 => {}", part1(lines_part_1));

    let lines_part_1 = read_file("../inputs/day_05.txt");
    println!("Day 05 - Part - 1 => {}", part1(lines_part_1));
}

fn part1(lines: Vec<String>) -> u32 {
    let mut value = 0;
    let mut seeds: Vec<u32> = lines[0].split(":").nth(1).unwrap().trim()
        .split_ascii_whitespace()
        .map(|x| x.trim().parse::<u32>().unwrap())
        .collect();

    let mut in_seed_to_soil_map = false;
    let mut in_soil_to_fertilizer_map = false;
    let mut in_fertilizer_to_water_map = false;
    let mut in_water_to_light_map = false;
    let mut in_light_to_temperature_map = false;
    let mut in_temperature_to_humidity_map = false;
    let mut in_humidity_to_location_map = false;

    let mut seed_to_soil_map: Vec<(u32,u32,u32)> = vec![];
    let mut soil_to_fertilizer_map: Vec<(u32,u32,u32)> = vec![];
    let mut fertilizer_to_water_map: Vec<(u32,u32,u32)> = vec![];
    let mut water_to_light_map: Vec<(u32,u32,u32)> = vec![];
    let mut light_to_temperature_map: Vec<(u32,u32,u32)> = vec![];
    let mut temperature_to_humidity_map: Vec<(u32,u32,u32)> = vec![];
    let mut humidity_to_location_map: Vec<(u32,u32,u32)> = vec![];

    let mut map_counter = 0;
    for i in 0..lines.len() {

    }

    return 0;
}

fn part2(lines: Vec<String>) -> u32 {
    for i in 0..lines.len() {
        let line = &lines[i];
    }
    return 0;
}

#[cfg(test)]
mod day_05_tests {
    use crate::day_05::{part1, part2};
    use crate::utils::read_file;

    #[test]
    fn part_1_example_cases() {
        let lines_part_1: Vec<String> = vec![

        ];
        assert_eq!(13, part1(lines_part_1))
    }

    #[test]
    fn part_1_full_cases() {
        let lines_part_1 = read_file("../inputs/day_05.txt");
        assert_eq!(0, part1(lines_part_1))
    }

    #[test]
    fn part_2_full_cases() {
        let lines_part_2 = read_file("../inputs/day_05.txt");
        assert_eq!(5659035, part2(lines_part_2))
    }

    #[test]
    fn part_2_example_cases() {
        let lines_part_2: Vec<String> = vec![
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53".to_string(),
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19".to_string(),
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1".to_string(),
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83".to_string(),
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36".to_string(),
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11".to_string(),
        ];
        assert_eq!(30, part2(lines_part_2))
    }
}
