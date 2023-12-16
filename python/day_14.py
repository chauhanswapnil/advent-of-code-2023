def read_file_as_string(file_path: str):
    with open(file_path, 'r') as file:
        return file.read()


def part1():
    inputs = read_file_as_string("../inputs/day_14.txt")
    grid = inputs.splitlines()
    grid = list(map("".join, zip(*grid)))
    grid = ["#".join(["".join(sorted(list(group), reverse=True)) for group in row.split("#")]) for row in grid]
    grid = list(map("".join, zip(*grid)))
    print(sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid)))


def part2():
    inputs = read_file_as_string("../inputs/day_14.txt")
    grid = tuple(inputs.splitlines())
    seen = {grid}
    array = [grid]
    iter = 0
    while True:
        iter += 1
        grid = cycle(grid)
        if grid in seen:
            break
        seen.add(grid)
        array.append(grid)
    first = array.index(grid)
    grid = array[(1000000000 - first) % (iter - first) + first]
    print(sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid)))


def cycle(grid):
    for _ in range(4):
        grid = tuple(map("".join, zip(*grid)))
        grid = tuple("#".join(["".join(sorted(tuple(group), reverse=True)) for group in row.split("#")]) for row in grid)
        grid = tuple(row[::-1] for row in grid)
    return grid


if __name__ == "__main__":
    part1()
    part2()
