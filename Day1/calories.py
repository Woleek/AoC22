"""Advent of Code 2022 - Day 1 Solution"""
INPUT_FILE = r"Day1\input.txt"


def load_input(file_path: str) -> list:
    """Loads input data from txt file

    Args:
        input_file (str): file name

    Returns:
        list: list of file contents line by line
    """
    with open(file_path, mode='r', encoding="UTF-8") as file:
        return file.read().rstrip().split('\n')


def pack_elves(items: list) -> dict:
    """Calculate calories carried by each elf

    Args:
        items_list (list): list of items (calories)

    Returns:
        dict: number of an elf with calories carried
    """
    elves = {}
    elf_number = 1
    calories = 0
    for item in items:
        if not item:
            elves[str(elf_number)] = calories
            elf_number += 1
            calories = 0
        else:
            calories += int(item)
    return elves


def get_most_calories(elves: dict) -> int:
    """Part 1 solution:
    Find elve with most calories carried

    Args:
        elves (dict): number of an elf with calories carried

    Returns:
        int: most calories carried by an elf
    """
    calories_list = list(elves.values())
    return max(calories_list)


def get_three_most_caories(elves: dict) -> int:
    """Part 2 solution:
    Find three elve with most calories carried

    Args:
        elves (dict): number of an elf with calories carried

    Returns:
        int: calories carried by top three elves carring most calories
    """
    calories_list = list(elves.values())
    most_three = 0
    for _ in range(3):
        curr_most = max(calories_list)
        most_three += curr_most
        calories_list.remove(curr_most)
    return most_three


if __name__ == "__main__":
    items_list = load_input(INPUT_FILE)
    elves_packed = pack_elves(items_list)
    print(f"Part 1 answer: {get_most_calories(elves_packed)}")
    print(f"Part 2 answer: {get_three_most_caories(elves_packed)}")
