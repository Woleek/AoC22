"""Advent of Code 2022 - Day 9 Solution"""
from math import atan2, pi

INPUT_FILE = "Day9/input.txt"

def load_input(file_path: str) -> list:
    """Loads input data from txt file

    Args:
        input_file (str): file name

    Returns:
        list: list of file contents line by line
    """
    with open(file_path, mode='r', encoding="UTF-8") as file:
        return file.read().rstrip().split('\n')

def check_touching(first: tuple, second: tuple) -> bool:
    """Check if knots are touching each other

    Args:
        first (tuple): coordinates of 1st knot
        second (tuple): coordinates of 2nd knot

    Returns:
        bool: True if knots are touching, else False
    """
    distance = (first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2
    return distance <= 2

def move_knot(direction: str, knot: tuple) -> tuple:
    """Move knot to new coordinates

    Args:
        direction (str): direction of movemnet
        knot (tuple): old coordinates of knot

    Returns:
        tuple: new coordinates of knot
    """
    match direction:
        case 'R ':
            knot = (knot[0] + 1, knot[1])
        case 'L ':
            knot = (knot[0] - 1, knot[1])
        case 'U ':
            knot = (knot[0], knot[1] + 1)
        case 'D ':
            knot = (knot[0], knot[1] - 1)
        case 'UR':
            knot = (knot[0] + 1, knot[1] + 1)
        case 'UL':
            knot = (knot[0] - 1, knot[1] + 1)
        case 'DR':
            knot = (knot[0] + 1, knot[1] - 1)
        case 'DL':
            knot = (knot[0] - 1, knot[1] - 1)
    return knot

def check_direction(first: tuple, second: tuple) -> str:
    """Check direction from first to second knot

    Args:
        first (tuple): coordinates of 1st knot
        second (tuple): coordinates of 2nd knot

    Returns:
        str: direction from first to second
    """
    delta_x = second[0] - first[0]
    delta_y = second[1] - first[1]
    angle_rad = atan2(delta_x, delta_y)
    angle_deg = angle_rad*180.0/pi
    if angle_deg == 0.0 or angle_deg == 360.0:
        return 'U '
    if 0.0 < angle_deg < 90.0:
        return 'UR'
    if angle_deg == 90.0:
        return 'R '
    if 90.0 < angle_deg < 180.0:
        return 'DR'
    if angle_deg == 180.0:
        return 'D '
    if -90.0 > angle_deg:
        return 'DL'
    if angle_deg == -90.0:
        return 'L '
    if 0.0 > angle_deg > -90.0:
        return 'UL'

def count_visited(list_of_moves: list, n_knots: int) -> int:
    """Count spaces visited by tail knot at least once during movemnet

    Args:
        list_of_moves (list): sequence of head moves
        n_knots (int): number of knots

    Returns:
        int: number of visited spaces
    """
    knots = [(0, 0) for _ in range(n_knots)]
    visited_list = set()
    visited_list.add(knots[-1])
    for move in list_of_moves:
        distance = ''.join(filter(str.isdigit, move))
        for _ in range(int(distance)):
            knots[0] = move_knot(move[0 : 2], knots[0])
            for idx in range(1, n_knots):
                is_touching = check_touching(knots[idx], knots[idx-1])
                if not is_touching:
                    direction = check_direction(knots[idx], knots[idx-1])
                    knots[idx] = move_knot(direction, knots[idx])
            visited_list.add(knots[-1])
    return len(visited_list)

if __name__ == '__main__':
    input_list = load_input(INPUT_FILE)
    print(f"Part 1 answer: {count_visited(input_list, 2)}")
    print(f"Part 2 answer: {count_visited(input_list, 10)}")
