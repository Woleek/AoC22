"""Advent of Code 2022 - Day 11 Solution"""
import re
from math import prod

INPUT_FILE = "Day11/input.txt"

def load_input(file_path: str) -> list:
    """Loads input data from txt file

    Args:
        input_file (str): file name

    Returns:
        list: list of file contents line by line
    """
    with open(file_path, mode='r', encoding="UTF-8") as file:
        return file.read().rstrip().split('\n')
    
def init_monkey(monkey_lines: list) -> dict:
    """Initializes dict of monkey attributes

    Args:
        monkey_lines (list): lines of monkey attributes input

    Returns:
        dict: monkeys initialized
    """
    monkey_attrs = {}
    monkey_attrs['items'] = [int(item) for item in re.findall("\d+", monkey_lines[0])]
    monkey_attrs['operation'] = monkey_lines[1][monkey_lines[1].index('=')+2 : ]
    monkey_attrs['test'] = [int(re.search("\d+", test_line).group()) for test_line in monkey_lines[2 : ]]
    monkey_attrs['inspected'] = 0
    return monkey_attrs

def find_monkeys(input_lines: list) -> tuple:
    """Initializes dict of monkeys from input, calculates worry modulo

    Args:
        input_lines (list): lines of input from file

    Returns:
        tuple: dict of monkeys, worry_modulo (for keeping worry level managable)
    """
    monkeys = {}
    for lines in [input_lines[idx : idx+6] for idx in range(0, len(input_lines), 7)]:
        monkey_number = int(re.search("\d+", lines[0]).group())
        monkeys[monkey_number] = init_monkey(lines[1 : ])
    worry_modulo = prod(monkey['test'][0] for monkey in monkeys.values())
    return monkeys, worry_modulo

def play_keep_away(monkeys: dict, worry_modulo: int, rounds: int, lower_worry: int) -> dict:
    """Playes keep away with given conditions and dict of monkeys

    Args:
        monkeys (dict): monkeys playing game
        worry_modulo (int): keeps worry level managable
        rounds (int): number of rounds to play
        lower_worry (int): divisor to lower worry level

    Returns:
        dict: monkeys dict state after game
    """
    for _ in range(rounds):
        for monkey in monkeys.values():
            for item in monkey['items']:
                monkey['inspected'] += 1
                worry = eval(monkey['operation'], {'old': item}) % worry_modulo
                worry = worry // lower_worry
                if worry % monkey['test'][0] == 0:
                    monkeys[monkey['test'][1]]['items'].append(worry)
                else:
                    monkeys[monkey['test'][2]]['items'].append(worry)
            monkey['items'].clear()
    return monkeys

def calc_score(monkeys: dict) -> int:
    """Calculates score of given monkey dict state

    Args:
        monkeys (dict): dict of monekys

    Returns:
        int: score - level of monkeys bussiness
    """
    inspected = sorted([monkey['inspected'] for monkey in monkeys.values()], reverse=True)
    return inspected[0] * inspected[1]

if __name__ == '__main__':
    lines_of_input = load_input(INPUT_FILE)
    monkeys_list1, modulo = find_monkeys(lines_of_input)
    monkeys_part1 = play_keep_away(monkeys_list1, modulo, rounds=20, lower_worry=3)
    print(f"Part 1 answer: {calc_score(monkeys_part1)}")

    monkeys_list2, modulo = find_monkeys(lines_of_input)
    monkeys_part2 = play_keep_away(monkeys_list2, modulo, rounds=10000, lower_worry=1)
    print(f"Part 2 answer: {calc_score(monkeys_part2)}")
    