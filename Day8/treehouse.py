"""Advent of Code 2022 - Day 8 Solution"""
import numpy as np

INPUT_FILE = "Day8/input.txt"

def load_input(file_path: str) -> list:
    """Loads input data from txt file

    Args:
        input_file (str): file name

    Returns:
        list: list of file contents line by line
    """
    with open(file_path, mode='r', encoding="UTF-8") as file:
        return file.read().rstrip().split('\n')

def input_to_matrix(lines: list) -> np.ndarray:
    """Converts lines of input to forrest grid (matrix)

    Args:
        lines (list): lines of input

    Returns:
        np.ndarray: forrest of int sizes
    """
    grid = np.zeros((len(lines), len(lines[0])), dtype=int)
    for x, line in enumerate(lines):
        for y, value in enumerate(line):
            grid[x][y] = int(value)
    return grid

def check_visible(grid: np.ndarray, x: int, y: int) -> bool:
    """Check if current tree is visible

    Args:
        grid (np.ndarray): forrest of int sizes
        x (int): x coordinate
        y (int): y coordinate

    Returns:
        bool: True if tree is visible, else False
    """
    size = grid[x][y]
    sides = grid[0 : x, y], grid[x+1 : , y], grid[x, 0 : y], grid[x, y+1 : ]
    visible_sides = [True for _ in range(4)]
    for idx, side in enumerate(sides):
        for value in side:
            if value >= size:
                visible_sides[idx] = False
    return any(visible_sides)

def count_visible(grid: np.ndarray) -> int:
    """Counts number of visible trees in forrest from outside

    Args:
        grid (np.ndarray): forrest of int sizes

    Returns:
        int: number of visible trees
    """
    visible_counter = (grid.shape[0] + grid.shape[0] - 2) * 2
    for x in range(1, grid.shape[0]-1):
        for y in range(1, grid.shape[1]-1):
            if check_visible(grid, x, y):
                visible_counter += 1
    return visible_counter

def calc_scenic_score(grid: np.ndarray, x: int, y: int) -> int:
    """Caculates scenic score for current tree

    Args:
        grid (np.ndarray): forrest of int sizes
        x (int): x coordinate
        y (int): y coordinate

    Returns:
        int: tree scenic score
    """
    size = grid[x][y]
    sides = grid[x-1 : : -1, y], grid[x+1 : , y], grid[x, y-1 : : -1], grid[x, y+1 : ]
    sides_scores = [0 for _ in range(4)]
    for idx, side in enumerate(sides):
        side_score = 0
        for value in side:
            side_score += 1
            if value >= size:
                break

        sides_scores[idx] = side_score
        result = 1
    for score in sides_scores:
        result *= score
    return result

def find_max_scenic_score(grid: np.ndarray) -> int:
    """Find max scenic score in forrest

    Args:
        grid (np.ndarray): forrest of int sizes

    Returns:
        int: max scenic score
    """
    max_score = 0
    for x in range(1, grid.shape[0]-1):
        for y in range(1, grid.shape[1]-1):
            curr_score = calc_scenic_score(grid, x, y)
            if curr_score > max_score:
                max_score = curr_score
    return max_score

if __name__ == '__main__':
    input_lines = load_input(INPUT_FILE)
    forrest = input_to_matrix(input_lines)
    print(f"Part 1 answer: {count_visible(forrest)}")
    print(f"Part 2 answer: {find_max_scenic_score(forrest)}")
    