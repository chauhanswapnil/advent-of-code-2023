use crate::utils::read_file;

pub fn day_03() {
    let lines_part_1 = read_file("../inputs/day_03_part_1.txt");
    println!("Part - 1 => {}", part1(lines_part_1));
    let lines_part_2 = read_file("../inputs/day_03_part_1.txt");
    println!("Part - 2 => {}", part2(lines_part_2));
}

#[derive(Debug)]
struct Symbol {
    symbol: char,
    symbol_position: (u32, u32),
    affecting_positions: Vec<(u32, u32)>
}

#[derive(Debug)]
struct Number {
    number: u32,
    number_positions: Vec<(u32,u32)>
}


fn part1(lines: Vec<String>) -> u32 {
    let mut affecting_positions: Vec<(u32,u32)> = vec![];

    for (i, line) in lines.iter().enumerate() {
        for (j, character) in line.char_indices() {
            if !character.is_ascii_digit() && character != '.' {
                affecting_positions.push(((i - 1) as u32, (j - 1) as u32));
                affecting_positions.push((i as u32, (j - 1) as u32));
                affecting_positions.push(((i + 1) as u32, (j - 1) as u32));
                affecting_positions.push(((i - 1) as u32, (j + 1) as u32));
                affecting_positions.push((i as u32, (j + 1) as u32));
                affecting_positions.push(((i + 1) as u32, (j + 1) as u32));
                affecting_positions.push(((i - 1) as u32, j as u32));
                affecting_positions.push((i as u32, j as u32));
                affecting_positions.push(((i + 1) as u32, j as u32));
            }
        }
    }

    let mut total_sum:u32 = 0;

    for (i, line) in lines.iter().enumerate() {
        let mut current_num :String = String::new();
        let mut number_pos:Vec<(u32, u32)> = vec![];
        for (j, character) in line.char_indices() {
            if character.is_ascii_digit() {
                number_pos.push((i as u32, j as u32));
                current_num += &String::from(character);
            } else {
                if current_num != "" {
                    if  number_pos.iter()
                        .any(|&x| affecting_positions.contains(&x)) {
                        total_sum = total_sum + (current_num.parse::<u32>().unwrap());
                    }
                    number_pos = vec![];
                }
                current_num = String::new();
            }
        }
    }

    return total_sum;
}

fn part2(lines: Vec<String>) -> u32 {
    let mut symbols: Vec<Symbol> = vec![];;
    for (i, line) in lines.iter().enumerate() {
        let mut affecting_positions: Vec<(u32,u32)> = vec![];
        for (j, character) in line.char_indices() {
            if character == '*' {
                affecting_positions.push(((i - 1) as u32, (j - 1) as u32));
                affecting_positions.push((i as u32, (j - 1) as u32));
                affecting_positions.push(((i + 1) as u32, (j - 1) as u32));
                affecting_positions.push(((i - 1) as u32, (j + 1) as u32));
                affecting_positions.push((i as u32, (j + 1) as u32));
                affecting_positions.push(((i + 1) as u32, (j + 1) as u32));
                affecting_positions.push(((i - 1) as u32, j as u32));
                affecting_positions.push((i as u32, j as u32));
                affecting_positions.push(((i + 1) as u32, j as u32));

                let symbol = Symbol {
                    symbol: character,
                    symbol_position: (i as u32, j as u32),
                    affecting_positions: affecting_positions.clone(),
                };
                symbols.push(symbol);
            }
        }
    }

    let mut total_sum:u32 = 0;
    let mut numbers:Vec<Number> = vec![];

    for (i, line) in lines.iter().enumerate() {
        let mut current_num :String = String::new();
        let mut number_pos:Vec<(u32, u32)> = vec![];

        for (j, character) in line.char_indices() {
            if character.is_ascii_digit() {
                number_pos.push(((i as u32), (j as u32)));
                current_num += &String::from(character);
            } else {
                if current_num != "" {
                    let number = Number {
                        number: current_num.parse::<u32>().unwrap(),
                        number_positions: number_pos.clone(),
                    };
                    numbers.push(number);
                    number_pos = vec![];
                }
                current_num = String::new();
            }
        }
    }
    // println!("{:?}", symbols);
    // println!("{:?}", numbers);
    for symbol in &symbols {
        let mut matched_nums: Vec<u32> = vec![];
        for number in &numbers {
            // Find intersection of number.number_positions and symbol.affecting_positions
            if  number.number_positions.iter()
                .any(|&x| symbol.affecting_positions.contains(&x)) {
                matched_nums.push(number.number);
            }
        }
        if matched_nums.len() == 2 {
            total_sum = total_sum + (matched_nums[0] * matched_nums[1])
        }
    }

    return total_sum;
}

#[cfg(test)]
mod day_03_tests {
    use crate::day_03::{part1, part2};
    use crate::utils::read_file;

    #[test]
    fn part_1_example_cases() {
        let lines_part_1: Vec<String> = vec![
            "467..114..".to_string(), // (0,1,2)  (5,6,7)
            "...*......".to_string(), // 3
            "..35..633.".to_string(), // (2,3) (6,7,8)
            "......#...".to_string(), // 6
            "617*......".to_string(), // (0,1,2) 3
            ".....+.58.".to_string(), // 5 (7,8)
            "..592.....".to_string(), // (2,3,4)
            "......755.".to_string(), // (6,7,8)
            "...$.*....".to_string(), // 3 5
            ".664.598..".to_string(), // (1,2,3) (5,6,7)
        ];
        assert_eq!(4361, part1(lines_part_1))
    }

    #[test]
    fn part_1_full_cases() {
        let lines_part_1 = read_file("../inputs/day_03_part_1.txt");
        assert_eq!(528799, part1(lines_part_1))
    }

    #[test]
    fn part_2_full_cases() {
        let lines_part_2 = read_file("../inputs/day_03_part_2.txt");
        assert_eq!(84907174, part2(lines_part_2))
    }

    #[test]
    fn part_2_example_cases() {
        let lines_part_2: Vec<String> = vec![
            "467..114..".to_string(), // (0,1,2)  (5,6,7)
            "...*......".to_string(), // 3
            "..35..633.".to_string(), // (2,3) (6,7,8)
            "......#...".to_string(), // 6
            "617*......".to_string(), // (0,1,2) 3
            ".....+.58.".to_string(), // 5 (7,8)
            "..592.....".to_string(), // (2,3,4)
            "......755.".to_string(), // (6,7,8)
            "...$.*....".to_string(), // 3 5
            ".664.598..".to_string(), // (1,2,3) (5,6,7)
        ];
        assert_eq!(467835, part2(lines_part_2))
    }
}
