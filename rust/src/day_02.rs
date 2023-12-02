use crate::utils::read_file;

const MAX_RED_POSSIBLE: u32 = 12;
const MAX_GREEN_POSSIBLE: u32 = 13;
const MAX_BLUE_POSSIBLE: u32 = 14;

pub fn day_02() {
    let lines_part_1 = read_file("../inputs/day_02_part_1.txt");
    println!("Part - 1 => {}", part1(lines_part_1));
    let lines_part_2 = read_file("../inputs/day_02_part_1.txt");
    println!("Part - 2 => {}", part2(lines_part_2));
}

fn part2(lines: Vec<String>) -> u32 {
    let mut total_power = 0;
    for line in lines {
        let game = process_line(line.as_str());
        let mut minimum_red: u32 = 1;
        let mut minimum_green: u32 = 1;
        let mut minimum_blue: u32 = 1;
        for revealed_subset in game.revealed {
            if revealed_subset.red.unwrap_or(1) > minimum_red {
                minimum_red = revealed_subset.red.unwrap_or(1);
            }
            if revealed_subset.green.unwrap_or(0) > minimum_green {
                minimum_green = revealed_subset.green.unwrap_or(1);
            }
            if revealed_subset.blue.unwrap_or(0) > minimum_blue {
                minimum_blue = revealed_subset.blue.unwrap_or(1);
            }
        }
        total_power = total_power + (minimum_red * minimum_green * minimum_blue);
    }
    return total_power;
}

fn part1(lines: Vec<String>) -> u32 {
    let mut sum_of_impossible_ids = 0;
    let mut sum_of_all_ids = 0;
    for line in lines {
        let game = process_line(line.as_str());
        for revealed_subset in game.revealed {
            if revealed_subset.red > Some(MAX_RED_POSSIBLE) ||
                revealed_subset.green > Some(MAX_GREEN_POSSIBLE) ||
                revealed_subset.blue > Some(MAX_BLUE_POSSIBLE) {
                sum_of_impossible_ids += game.id;
                break;
            }
        }
        sum_of_all_ids += game.id;
    }
    return sum_of_all_ids - sum_of_impossible_ids;
}

#[derive(Debug)]
struct Game {
    id: u32,
    revealed: Vec<RevealedSubsets>
}

#[derive(Debug)]
struct RevealedSubsets {
    red: Option<u32>,
    green: Option<u32>,
    blue: Option<u32>,
}

fn process_line(line: &str) -> Game {
    let mut iter = line.split(":");
    let id: u32 = iter.next().unwrap().trim().split(" ").collect::<Vec<_>>()[1].parse::<u32>().unwrap();

    let subsets = iter.next().unwrap().trim();
    let revealed = subsets.split(';').map(|subset| {
        let counts: Vec<_> = subset.trim().split(',').map(|count_color| {
            let parts: Vec<_> = count_color.trim().split(' ').collect();
            let count = parts[0].parse::<u32>().unwrap();
            let color = parts[1].to_lowercase();
            return (count, color);
        }).collect();

        let mut revealed_subset = RevealedSubsets {
            red: None,
            green: None,
            blue: None,
        };
        for (count, color) in counts {
            match color.as_str() {
                "red" => revealed_subset.red = Some(count),
                "green" => revealed_subset.green = Some(count),
                "blue" => revealed_subset.blue = Some(count),
                _ => {} // No other colors for now
            }
        }
        return revealed_subset;
    }).collect();
    return Game {id, revealed};
}


#[cfg(test)]
mod day_02_tests {
    use crate::day_02::part1;
    use crate::day_02::part2;

    #[test]
    fn part_1_example_cases() {
        let lines: Vec<String> = vec![
            "Game 1: 3 blue, 4 Red; 1 Red, 2 green, 6 blue; 2 green".to_string(),
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 Red; 1 green, 1 blue".to_string(),
            "Game 3: 8 green, 6 blue, 20 Red; 5 blue, 20 Red, 13 green; 5 green, 1 Red".to_string(),
            "Game 4: 1 green, 3 Red, 6 blue; 3 green, 6 Red; 3 green, 15 blue, 14 Red".to_string(),
            "Game 5: 6 Red, 1 blue, 3 green; 2 blue, 1 Red, 2 green".to_string(),
        ];
        assert_eq!(8, part1(lines))
    }

    #[test]
    fn part_2_example_cases() {
        let lines: Vec<String> = vec![
            "Game 1: 3 blue, 4 Red; 1 Red, 2 green, 6 blue; 2 green".to_string(),
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 Red; 1 green, 1 blue".to_string(),
            "Game 3: 8 green, 6 blue, 20 Red; 5 blue, 20 Red, 13 green; 5 green, 1 Red".to_string(),
            "Game 4: 1 green, 3 Red, 6 blue; 3 green, 6 Red; 3 green, 15 blue, 14 Red".to_string(),
            "Game 5: 6 Red, 1 blue, 3 green; 2 blue, 1 Red, 2 green".to_string(),
        ];
        assert_eq!(2286, part2(lines))
    }
}