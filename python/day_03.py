
def read_file(file_path: str):
    with open(file_path, 'r') as file:
        return file.readlines()


def part_1():
    positions_to_add = []
    lines = read_file("../inputs/day_03_part_1.txt")
    for i in range(0, len(lines)):
        line = lines[i]
        for j in range(0, len(line) - 1):
            char = line[j]
            if not char.isdigit() and char != ".":
                # Found Symbol, so now lets find all the bad positions to check for
                up_left = (i-1, j-1)
                left = (i, j-1)
                down_left = (i+1, j-1)

                up_right = (i-1, j+1)
                right = (i, j+1)
                down_right = (i+1, j+1)

                up = (i-1, j)
                main = (i, j)
                down = (i+1, j)

                positions_to_add.append(up_left)
                positions_to_add.append(left)
                positions_to_add.append(down_left)
                positions_to_add.append(up_right)
                positions_to_add.append(right)
                positions_to_add.append(down_right)
                positions_to_add.append(up)
                positions_to_add.append(main)
                positions_to_add.append(down)

    total_sum = 0
    for i in range(0, len(lines)):
        line = lines[i]
        current_num = ""
        number_pos = []
        for j in range(0, len(line)):
            char = line[j]
            if char.isdigit():
                number_pos.append((i, j))
                current_num += char
            else:
                if current_num:
                    # print(f"Found Number: {current_num}, Number Positions: {number_pos}")
                    if len(set(number_pos).intersection(set(positions_to_add))):
                        total_sum = total_sum + int(current_num)
                        # print(f"Add this Number {current_num}")
                    number_pos = []
                current_num = ""

    print(f"Total Sum is {total_sum}")


def part_2():
    positions_to_add = []
    lines = read_file("../inputs/day_03_part_1.txt")
    star_with_positions = []
    for i in range(0, len(lines)):
        line = lines[i]
        for j in range(0, len(line) - 1):
            char = line[j]
            if char == "*":
                # Found Symbol, so now lets find all the bad positions to check for
                up_left = (i-1, j-1)
                left = (i, j-1)
                down_left = (i+1, j-1)

                up_right = (i-1, j+1)
                right = (i, j+1)
                down_right = (i+1, j+1)

                up = (i-1, j)
                main = (i, j)
                down = (i+1, j)

                positions_to_add.append(up_left)
                positions_to_add.append(left)
                positions_to_add.append(down_left)
                positions_to_add.append(up_right)
                positions_to_add.append(right)
                positions_to_add.append(down_right)
                positions_to_add.append(up)
                positions_to_add.append(main)
                positions_to_add.append(down)

                star_with_positions.append({main: positions_to_add})
                # print(f"Symbol * with positions = {star_with_positions}")
                # print(f"Symbol = {char} ({i},{j}), Positions to Add = {positions_to_add}")
                positions_to_add = []

    total_sum = 0
    number_array = []
    number_positions = []
    for i in range(0, len(lines)):
        line = lines[i]
        current_num = ""
        number_pos = []
        for j in range(0, len(line)):
            char = line[j]
            if char.isdigit():
                number_pos.append((i, j))
                current_num += char
            else:
                if current_num:
                    # print(f"Found Number: {current_num}, Number Positions: {number_pos}")
                    number_array.append(int(current_num))
                    number_positions.append(number_pos)
                    number_pos = []
                current_num = ""
    # print(number_array)
    # print(number_positions)
    for star in star_with_positions:
        star_key = list(star.keys())[0]
        star_values: list = list(star.values())[0]
        matched_nums = []
        for i in range(0, len(number_array)):
            if len(set(number_positions[i]).intersection(set(star_values))):
                matched_nums.append(number_array[i])
                # print(f"Found number matching star {star_key} with value {number_array[i]}")
        if len(matched_nums) == 2:
            total_sum = total_sum + (matched_nums[0] * matched_nums[1])

        # For each star we check which numbers are gear parts for it and if they are more than 2,
        # we forget about that star
        # for
    print(f"Total Sum is {total_sum}")


if __name__ == "__main__":
    part_1()
    part_2()
