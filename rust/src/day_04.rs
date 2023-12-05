use std::collections::HashSet;
use crate::utils::read_file;

pub fn day_04() {
    let lines_part_1 = read_file("../inputs/day_04_part_1.txt");
    println!("Day 04 - Part - 1 => {}", part1(lines_part_1));

    let lines_part_1 = read_file("../inputs/day_04_part_1.txt");
    println!("Day 04 - Part - 1 => {}", part1(lines_part_1));
}

fn part1(lines: Vec<String>) -> u32 {

    let mut value = 0;
    for line in lines {

        let game = line.split(":")
            .nth(1)
            .unwrap();

        let winning = game.split(" | ")
            .nth(0)
            .unwrap();

        let ours = game.split(" | ")
            .nth(1)
            .unwrap()
            .trim();

        // println!("{winning:?} | {ours:?}");

        let winning_set: HashSet<u32> = winning
            .split_ascii_whitespace()
            .map(|x| x.trim().parse::<u32>().unwrap())
            .collect();

        let ours_set: HashSet<u32> = ours
            .split_ascii_whitespace()
            .map(|x| x.trim().parse::<u32>().unwrap())
            .collect();

        let winning: Vec<u32> = winning_set
            .intersection(&ours_set)
            .copied()
            .collect();

        if winning.len() > 0 {
            value += u32::pow(2, (winning.len() as u32) - 1);
        }
        // println!("{winning:?}")
    }
    return value;
}

fn part2(lines: Vec<String>) -> u32 {

    let mut played = vec![0; lines.len()];

    for i in 0..lines.len() {

        let line = &lines[i];

        played[i] += 1;

        let game = line.split(":")
            .nth(1)
            .unwrap();

        let winning = game.split(" | ")
            .nth(0)
            .unwrap();

        let ours = game.split(" | ")
            .nth(1)
            .unwrap()
            .trim();

        // println!("{winning:?} | {ours:?}");

        let winning_set: HashSet<u32> = winning
            .split_ascii_whitespace()
            .map(|x| x.trim().parse::<u32>().unwrap())
            .collect();

        let ours_set: HashSet<u32> = ours
            .split_ascii_whitespace()
            .map(|x| x.trim().parse::<u32>().unwrap())
            .collect();

        let winning_numbers: Vec<u32> = winning_set
            .intersection(&ours_set)
            .copied()
            .collect();

        for w in 0..winning_numbers.len() {
            played[i+w+1] += played[i];
        }
    }

    let sum: u32 = played.iter().sum();
    return sum;
}

#[cfg(test)]
mod day_04_tests {
    use crate::day_04::{part1, part2};
    use crate::utils::read_file;

    #[test]
    fn part_1_example_cases() {
        let lines_part_1: Vec<String> = vec![
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53".to_string(),
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19".to_string(),
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1".to_string(),
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83".to_string(),
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36".to_string(),
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11".to_string(),
        ];
        assert_eq!(13, part1(lines_part_1))
    }

    #[test]
    fn part_1_full_cases() {
        let lines_part_1 = read_file("../inputs/day_04_part_1.txt");
        assert_eq!(24160, part1(lines_part_1))
    }

    #[test]
    fn part_2_full_cases() {
        let lines_part_2 = read_file("../inputs/day_04_part_2.txt");
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
