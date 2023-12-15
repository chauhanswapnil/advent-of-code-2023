def read_file_as_string(file_path: str):
    with open(file_path, 'r') as file:
        return file.read()


def part1():
    inputs = read_file_as_string("../inputs/day_11.txt")
    grid = inputs.strip().splitlines()
    empty_rows = [r for r, row in enumerate(grid) if all(char == "." for char in row)]
    empty_cols = [c for c, col in enumerate(zip(*grid)) if all(char == "." for char in col)]

    position_galaxies = [(r, c) for r, row in enumerate(grid) for c, col in enumerate(row) if col == "#"]
    # print(position_galaxies)
    total = 0
    for i, (r1, c1) in enumerate(position_galaxies):
        for (r2, c2) in position_galaxies[:i]:
            for r in range(min(r1, r2), max(r1, r2)):
                total += 2 if r in empty_rows else 1
            for c in range(min(c1, c2), max(c1, c2)):
                total += 2 if c in empty_cols else 1

    print(total)


def part2():
    inputs = read_file_as_string("../inputs/day_11.txt")
    grid = inputs.strip().splitlines()
    empty_rows = [r for r, row in enumerate(grid) if all(char == "." for char in row)]
    empty_cols = [c for c, col in enumerate(zip(*grid)) if all(char == "." for char in col)]

    position_galaxies = [(r, c) for r, row in enumerate(grid) for c, col in enumerate(row) if col == "#"]
    # print(position_galaxies)
    total = 0
    for i, (r1, c1) in enumerate(position_galaxies):
        for (r2, c2) in position_galaxies[:i]:
            for r in range(min(r1, r2), max(r1, r2)):
                total += 1000000 if r in empty_rows else 1
            for c in range(min(c1, c2), max(c1, c2)):
                total += 1000000 if c in empty_cols else 1

    print(total)


if __name__ == "__main__":
    part1()
    part2()
