from math import lcm


def read_file_as_string(file_path: str):
    with open(file_path, 'r') as file:
        return file.read()


inputs = read_file_as_string("../inputs/day_08.txt")
INSTRUCTIONS = inputs.split("\n\n")[0]
# print(INSTRUCTIONS)

maps_list = list(inputs.split("\n\n")[1].split("\n"))
MAPS = {
    mapp.split("=")[0].strip(): tuple(mapp.split("=")[1].strip().strip('()').split(', '))
    for mapp in maps_list
}


# print(MAPS)

# def traverse(start: str, next_instruction_index: int, count=0):
#     left, right = MAPS[start]
#     if start == "ZZZ":
#         print(f"ZZZ found {count}")
#         return
#     if next_instruction_index == len(INSTRUCTIONS):
#         next_instruction_index = 0
#     if INSTRUCTIONS[next_instruction_index] == 'L':
#         traverse(left, next_instruction_index + 1, count + 1)
#     if INSTRUCTIONS[next_instruction_index] == 'R':
#         traverse(right, next_instruction_index + 1, count + 1)
#     return


def traverse_loop_part_1(start: str):  # recursion depth was exceeding
    count = 0
    index = 0

    while start != "ZZZ":
        left, right = MAPS[start]
        if INSTRUCTIONS[index] == 'L':
            start = left
        elif INSTRUCTIONS[index] == 'R':
            start = right
        count += 1
        index = (index + 1) % len(INSTRUCTIONS)

    print(f"Count {count}")


def part_1():
    # traverse("AAA", 0, 0)
    traverse_loop_part_1("AAA")


def traverse_loop_part_2(start: str):  # recursion depth was exceeding
    count = 0
    index = 0

    while not start.endswith("Z"):
        left, right = MAPS[start]
        if INSTRUCTIONS[index] == 'L':
            start = left
        elif INSTRUCTIONS[index] == 'R':
            start = right
        count += 1
        index = (index + 1) % len(INSTRUCTIONS)

    return count


def part_2():
    starts = list(filter(lambda x: x[2] == "A", MAPS))
    answers = [traverse_loop_part_2(start) for start in starts]
    print(lcm(*answers))


if __name__ == "__main__":
    part_1()
    part_2()
