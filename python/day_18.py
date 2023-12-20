def read_file_as_string(file_path: str):
    with open(file_path, 'r') as file:
        return file.read()


def calculate(dig_plan):
    points = [(0, 0)]
    directions = {
        "U": (-1, 0),
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1),
    }

    boundary_points = 0
    for line in dig_plan:
        d, n, _ = line.split()
        dr, dc = directions[d]
        n = int(n)
        boundary_points += n
        r, c = points[-1]
        points.append((r + dr * n, c + dc * n))
    # print(points)

    # Shoelace Formula to calculate an area of polygon -> https://en.wikipedia.org/wiki/Shoelace_formula
    # Since it calculates inside points, but we have coordinates as 1meter squared that means this will not be correct
    area = abs(sum(points[i][0] * (points[i-1][1] - points[(i+1) % len(points)][1]) for i in range(len(points)))) // 2
    print(area, boundary_points)
    # Instead we can use Picks Theorem to get the inner boundary points given an area and the boundary points of polygon
    # Picks Theorem -> https://en.wikipedia.org/wiki/Pick's_theorem
    interior_points = area - boundary_points // 2 + 1

    # Our required area will be sum of inner points and boundary points
    print(interior_points + boundary_points)


def part_1():
    inputs = read_file_as_string("../inputs/day_18.txt")
    dig_plan = inputs.splitlines()
    calculate(dig_plan)


def part_2():
    inputs = read_file_as_string("../inputs/day_18.txt")
    dig_plan = inputs.splitlines()
    true_grid = []
    for line in dig_plan:
        _, _, _hex = line.split()
        _hex = _hex[2:-1]
        n = str(int(_hex[:-1], 16))
        if _hex[-1] == "0":
            d = "R"
        elif _hex[-1] == "1":
            d = "D"
        elif _hex[-1] == "2":
            d = "L"
        else:
            d = "U"
        true_grid.append(" ".join([d, n, _hex]))
    calculate(true_grid)
    # print(true_grid)


if __name__ == "__main__":
    part_1()
    part_2()
