
def read_file(file_path: str):
    with open(file_path, 'r') as file:
        return file.readlines()


def part_1():
    lines = read_file("../inputs/day_01_part1.txt")
    total_sum = 0
    for line in lines:
        number_string = ""
        got_first = False
        last_digit_string = ""
        for char in line:
            if char.isdigit():
                if not got_first:
                    number_string = number_string + char
                    got_first = True
                last_digit_string = char
        number_string = number_string + last_digit_string
        total_sum = total_sum + int(number_string, 10)

    print(f"total_sum is {total_sum}")


def part_2():
    lines = read_file("../inputs/day_01_part2.txt")
    number_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    total_sum = 0

    for line in lines:
        got_first = False
        last_digit_str = ""
        number_string = ""

        for index, character in enumerate(line):
            if character.isdigit():
                if not got_first:
                    number_string += character
                    got_first = True
                last_digit_str = character

            # This gets the number word
            substring = line[index:]
            for word, number in number_map.items():
                if substring.startswith(word):
                    if not got_first:
                        # print(f"Matched Number {number}")
                        number_string += number
                        got_first = True
                    last_digit_str = number

        number_string += last_digit_str
        # print(f"Number is {number_string}")
        total_sum += int(number_string)

    print(f"Sum is {total_sum}")


if __name__ == "__main__":
    part_1()
    part_2()
