"""Advent of Code 2022 - Day 10 Solution"""

INPUT_FILE = "Day10/input.txt"

def load_input(file_path: str) -> list:
    """Loads input data from txt file

    Args:
        input_file (str): file name

    Returns:
        list: list of file contents line by line
    """
    with open(file_path, mode='r', encoding="UTF-8") as file:
        return file.read().rstrip().split('\n')

def calculate_signal_strenght(input_commands: list) -> int:
    """Calculates signal strenghts in given cycles

    Args:
        input_commands (list): list of commands

    Returns:
        int: sum of signal strenghts
    """
    x = 1
    cycle = 1
    signal_strenghts = []
    for command in input_commands:
        match command[ : 4]:
            case 'noop':
                cycle += 1
                if cycle in (20, 60, 100, 140, 180, 220):
                    signal_strenghts.append(cycle*x)
            case 'addx':
                cycle += 2
                if cycle-1 in (20, 60, 100, 140, 180, 220):
                    signal_strenghts.append((cycle-1)*x)
                x += int(command[5 : ])
                if cycle in (20, 60, 100, 140, 180, 220):
                    signal_strenghts.append(cycle*x)
    return sum(signal_strenghts)

def draw_pixel(cycle: int, sprite: int):
    """Prints pixel as '#' or '.' based on cycle number and sprite position

    Args:
        cycle (int): number of current cycle
        sprite (int): sprite's position
    """
    if cycle%40 in (sprite-1, sprite, sprite+1):
        print('#', end='')
    else:
        print('.', end='')

def check_row(cycle: int):
    """Jumps to new row if needed

    Args:
        cycle (int): number of current cycle
    """
    if cycle in (40, 80, 120, 160, 200):
        print('\n', end='')

def render_image(input_commands:list):
    """Prints next pixels based on input commands

    Args:
        input_commands (list): list of commands
    """
    sprite = 1
    cycle = 1
    draw_pixel(cycle-1, sprite)
    for command in input_commands:
        match command[ : 4]:
            case 'noop':
                cycle += 1
                draw_pixel(cycle-1, sprite)
                check_row(cycle)
            case 'addx':
                cycle += 1
                draw_pixel(cycle-1, sprite)
                check_row(cycle)
                cycle += 1
                sprite += int(command[5 : ])
                draw_pixel(cycle-1, sprite)
                check_row(cycle)

if __name__ == '__main__':
    input_lines = load_input(INPUT_FILE)
    print(f"Part 1 answer: {calculate_signal_strenght(input_lines)}")
    print("Part 2 answer:")
    render_image(input_lines)
