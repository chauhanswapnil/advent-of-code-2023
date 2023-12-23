from collections import deque


def read_file_as_string(file_path: str):
    with open(file_path, 'r') as file:
        return file.read()


def part_1():
    inputs = read_file_as_string("../inputs/day_21.txt")
    grid = inputs.splitlines()
    s = [(i, j) for i, row in enumerate(grid) for j, ch in enumerate(row) if ch == "S"][0]
    ans = set()
    seen = {s}
    q = deque([(s[0], s[1], 64)])
    while q:
        r, c, steps = q.popleft()
        if steps % 2 == 0:
            ans.add((r, c))
        if steps == 0:
            continue
        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == "#" or (nr, nc) in seen:
                continue
            seen.add((nr, nc))
            q.append((nr, nc, steps - 1))

    print(len(ans))


if __name__ == "__main__":
    part_1()
