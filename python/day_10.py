from collections import deque


def read_file_as_string(file_path: str):
    with open(file_path, 'r') as file:
        return file.read()


def part_1():
    inputs = read_file_as_string("../inputs/day_10.txt")
    grid = inputs.strip().splitlines()
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == "S":
                start_row = r
                start_col = c
                break
        else:
            continue
        break
    visited = {(start_row, start_col)}
    q = deque([(start_row, start_col)])

    while q:
        row, col = q.popleft()
        char = grid[row][col]
        if row > 0 and char in "S|JL" and grid[row-1][col] in "|7F" and (row-1, col) not in visited:
            visited.add((row-1, col))
            q.append((row-1, col))

        if row < len(grid) - 1 and char in "S|7F" and grid[row+1][col] in "|JL" and (row+1, col) not in visited:
            visited.add((row+1, col))
            q.append((row+1, col))

        if col > 0 and char in "S-J7" and grid[row][col-1] in "-LF" and (row, col-1) not in visited:
            visited.add((row, col-1))
            q.append((row, col-1))

        if col < len(grid[row]) - 1 and char in "S-LF" and grid[row][col+1] in "-J7" and (row, col+1) not in visited:
            visited.add((row, col+1))
            q.append((row, col+1))

    print(len(visited) // 2)


def part_2():
    inputs = read_file_as_string("../inputs/day_10.txt")
    grid = inputs.strip().splitlines()
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == "S":
                start_row = r
                start_col = c
                break
        else:
            continue
        break
    visited = {(start_row, start_col)}
    q = deque([(start_row, start_col)])
    maybe_s = {"|", "J", "L", "7", "F", "-"}
    while q:
        row, col = q.popleft()
        char = grid[row][col]
        if row > 0 and char in "S|JL" and grid[row-1][col] in "|7F" and (row-1, col) not in visited:
            visited.add((row-1, col))
            q.append((row-1, col))
            if char == "S":
                maybe_s &= {"|", "J", "L"}

        if row < len(grid) - 1 and char in "S|7F" and grid[row+1][col] in "|JL" and (row+1, col) not in visited:
            visited.add((row+1, col))
            q.append((row+1, col))
            if char == "S":
                maybe_s &= {"|", "7", "F"}

        if col > 0 and char in "S-J7" and grid[row][col-1] in "-LF" and (row, col-1) not in visited:
            visited.add((row, col-1))
            q.append((row, col-1))
            if char == "S":
                maybe_s &= {"-", "J", "7"}

        if col < len(grid[row]) - 1 and char in "S-LF" and grid[row][col+1] in "-J7" and (row, col+1) not in visited:
            visited.add((row, col+1))
            q.append((row, col+1))
            if char == "S":
                maybe_s &= {"-", "L", "F"}

    print(len(visited) // 2)
    (S,) = maybe_s
    print(S)
    grid = [row.replace("S", S) for row in grid]
    grid = ["".join(char if (r,c) in visited else "." for c, char in enumerate(row)) for r,row in enumerate(grid)]
    print("\n".join(grid))
    print()
    outside = set()
    for r, row in enumerate(grid):
        within = False
        up = None
        for c, char in enumerate(row):
            if char == "|":
                assert up is None
                within = not within
            elif char == "-":
                assert up is not None
            elif char in "LF":
                assert up is None
                up = (char == "L")
            elif char in "7J":
                assert up is not None
                if char != ("J" if up else "7"):
                    within = not within
                up = None
            elif char == ".":
                pass
            else:
                raise RuntimeError("Should not happen!")
            if not within:
                outside.add((r, c))
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            print("#" if (r, c) in outside-visited else ".", end="")
        print()

    print(len(grid) * len(grid[0]) - len(outside | visited))


if __name__ == "__main__":
    part_1()
    part_2()
