def read_file_as_string(file_path: str):
    with open(file_path, 'r') as file:
        return file.read()


def find_mirror1(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]  # Flip the top array
        below = grid[r:]
        above = above[:len(below)]
        below = below[:len(above)]
        if above == below:
            return r
    return 0


def part1():
    inputs = read_file_as_string("../inputs/day_13.txt")
    total = 0
    for block in inputs.split("\n\n"):
        grid = block.splitlines()
        row = find_mirror1(grid)
        total += row * 100
        col = find_mirror1(list(zip(*grid)))
        total += col
    print(total)


def find_mirror2(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]  # Flip the top array
        below = grid[r:]
        # We are looking for reflections that have only 1 difference between them
        # With zip we are iterating over both rows/cols of above and below at the same time
        if sum((sum(0 if a == b else 1 for a, b in zip(x, y))) for x, y in zip(above, below)) == 1:
            return r
    return 0


def part2():
    inputs = read_file_as_string("../inputs/day_13.txt")
    total = 0
    for block in inputs.split("\n\n"):
        grid = block.splitlines()
        row = find_mirror2(grid)
        total += row * 100
        col = find_mirror2(list(zip(*grid)))
        total += col
    print(total)


if __name__ == "__main__":
    part1()
    part2()
