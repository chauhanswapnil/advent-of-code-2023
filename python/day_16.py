from collections import deque


def read_file_as_string(file_path: str):
    with open(file_path, 'r') as file:
        return file.read()


def part1():
    inputs = read_file_as_string("../inputs/day_16.txt")
    grid = inputs.splitlines()
    # [(r, c, dr, dc)]
    start = [(0, -1, 0, 1)]
    visited = set()
    q = deque(start)
    while q:
        r, c, dr, dc = q.popleft()
        r += dr
        c += dc

        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            continue

        current = grid[r][c]

        if current == "." or (current == "-" and dc != 0) or (current == "|" and dr != 0):
            if (r, c, dr, dc) not in visited:
                visited.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif current == "/":
            dr, dc = -dc, -dr
            if (r, c, dr, dc) not in visited:
                visited.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif current == "\\":
            dr, dc = dc, dr
            if (r, c, dr, dc) not in visited:
                visited.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        else:
            for dr, dc in [(1, 0), (-1, 0)] if current == "|" else [(0, 1), (0, -1)]:
                if (r, c, dr, dc) not in visited:
                    visited.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))
    unique_visited = {(r, c) for (r, c, _, _) in visited}
    # print(visited)
    print(len(unique_visited))


def part2():
    inputs = read_file_as_string("../inputs/day_16.txt")
    grid = inputs.splitlines()
    max_value = 0
    for r in range(len(grid)):
        max_value = max(max_value, calculate(grid, r, -1, 0, 1))
        max_value = max(max_value, calculate(grid, r, len(grid[0]), 0, 1))
    for c in range(len(grid)):
        max_value = max(max_value, calculate(grid, -1, c, 0, 1))
        max_value = max(max_value, calculate(grid, len(grid), c, 0, 1))
    print(max_value)


def calculate(grid, r, c, dr, dc):
    start = [(r, c, dr, dc)]
    visited = set()
    q = deque(start)
    while q:
        r, c, dr, dc = q.popleft()
        r += dr
        c += dc

        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            continue

        current = grid[r][c]

        if current == "." or (current == "-" and dc != 0) or (current == "|" and dr != 0):
            if (r, c, dr, dc) not in visited:
                visited.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif current == "/":
            dr, dc = -dc, -dr
            if (r, c, dr, dc) not in visited:
                visited.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif current == "\\":
            dr, dc = dc, dr
            if (r, c, dr, dc) not in visited:
                visited.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        else:
            for dr, dc in [(1, 0), (-1, 0)] if current == "|" else [(0, 1), (0, -1)]:
                if (r, c, dr, dc) not in visited:
                    visited.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))
    unique_visited = {(r, c) for (r, c, _, _) in visited}
    return len(unique_visited)


if __name__ == "__main__":
    part1()
    part2()
