def read_file_as_string(file_path: str):
    with open(file_path, 'r') as file:
        return file.read()


def part_1():
    inputs = read_file_as_string("../inputs/day_10.txt")
    lines = inputs.split("\n")
    matrix = []
    for i in range(0, len(lines)):
        row = []
        for j in range(0, len(lines[i])):
            if lines[i][j] == "S":
                start_pos = (i, j)
            row.append(lines[i][j])
        matrix.append(row)
    # print(matrix)
    # Brute force. Go in Every Direction
    dfs(matrix, start_pos)


def dfs(matrix, start):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and not visited[x][y]

    def dfs_helper(current, prev=None):
        # Mark the current cell as visited
        x, y = current
        directions = []
        if not prev:
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if prev:
            print(f"Previous: {prev}")
            px, py = prev
        visited[x][y] = True

        print(f"Matrix Value at {(x, y)}: {matrix[x][y]}")

        current_char = matrix[x][y]
        # Define the possible directions
        if current_char == '|':
            directions = [(-1, 0), (1, 0)]
        elif current_char == '-':
            directions = [(0, -1), (0, 1)]
        elif current_char == 'L':
            directions = [(0, 1), (-1, 0)]
        elif current_char == 'J':
            directions = [(0, -1), (-1, 0)]
        elif current_char == '7':
            directions = [(1, 0), (-1, 0)]
        elif current_char == 'F':
            directions = [(1, 0), (0, 1)]
        elif current_char == '.':
            directions = []

        # Explore neighbors
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                dfs_helper(current=(new_x, new_y), prev=(x, y))

    # Start DFS from the given position
    dfs_helper(start)


if __name__ == "__main__":
    part_1()
