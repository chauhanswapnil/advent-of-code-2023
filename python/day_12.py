def read_file_as_string(file_path: str):
    with open(file_path, 'r') as file:
        return file.read()


def part1():
    inputs = read_file_as_string("../inputs/day_12.txt")
    print(inputs)


if __name__ == "__main__":
    part1()
