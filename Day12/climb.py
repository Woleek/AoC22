"""Advent of Code 2022 - Day 12 Solution"""
from collections import deque

INPUT_FILE = "Day12/input.txt"

def load_input(file_path: str) -> list:
    """Loads input data from txt file

    Args:
        input_file (str): file name

    Returns:
        list: list of file contents line by line
    """
    with open(file_path, mode='r', encoding="UTF-8") as file:
        return file.read().rstrip().split('\n')

def climb(grid: list, *start_points: str) -> int:
    """Calculates shorthest path to climb from any of start_points to 'E'

    Args:
        grid (list): hills map from input
        start_points (str): points to start climbing

    Returns:
        int: shorthest path
    """
    hills = deque((x, y, 0, 'a') for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] in start_points)
    visited = set((x, y) for x, y, _, _ in hills)

    def walk(x: int, y: int, length: int, point: str):
        """Used to find if next point is possible to walk to from current one

        Args:
            x (int): x coordinate in grid
            y (int): x coordinate in grid
            length (int): lenght of current path
            point (str): elevation of current point
        """
        if not (0 <= x < len(grid)) or not 0 <= y < len(grid[0]):
            return
        if (x, y) in visited:
            return
        next_point = grid[x][y].replace('E', 'z')
        if ord(next_point) > ord(point) + 1:
            return
        visited.add((x, y))
        hills.append((x, y, length + 1, next_point))

    while len(hills):
        x, y, length, point = hills.popleft()
        if grid[x][y] == 'E':
            return length
        walk(x + 1, y, length, point)
        walk(x - 1, y, length, point)
        walk(x, y + 1, length, point)
        walk(x, y - 1, length, point)

if __name__ == '__main__':
    input_lines = load_input(INPUT_FILE)
    print(f"Part 1 answer: {climb(input_lines, 'S')}")
    print(f"Part 2 answer: {climb(input_lines, 'S', 'a')}")
