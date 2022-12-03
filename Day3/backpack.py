"""Advent of Code 2022 - Day 3 Solution"""
INPUT_FILE = r"Day3\input.txt"

def load_input(file_path: str) -> list:
    """Loads input data from txt file

    Args:
        input_file (str): file name

    Returns:
        list: list of file contents line by line
    """
    with open(file_path, mode='r', encoding="UTF-8") as file:
        return file.read().split('\n')

def find_same_item(backpack: str) -> str:
    """Finds common item in two compartments of backpack

    Args:
        backpack (str): items in backpack

    Returns:
        str: common item
    """
    first_compartment, second_compartment = set(backpack[:int(len(backpack)/2)]), \
                                            set(backpack[int(len(backpack)/2):])

    common_item = first_compartment & second_compartment
    common_item = ''.join(common_item)
    return common_item

def prioritize(item:str) -> int:
    """Calculates priority of an item

    Args:
        item (str): item name

    Returns:
        int: calcu;ated priority
    """
    if str(item).islower():
        value = ord(item) - 96 # a-z: 1-27
    else:
        value = ord(item) - 38 # A-Z: 28-52
    return value

def identify_group(*group_backpacks:str) -> str:
    """Identifies common item for group of three backpacks

    Args:
        group_backpacks (tuple[str]): group of backpacks

    Returns:
        str: common item (badge) for group
    """
    backpack_1 = set(group_backpacks[0])
    backpack_2 = set(group_backpacks[1])
    backpack_3 = set(group_backpacks[2])

    badge = backpack_1 & backpack_2 & backpack_3
    badge = ''.join(badge)
    return badge

if __name__ == '__main__':
    backpacks = load_input(INPUT_FILE)
    misplaced_items = [find_same_item(backpack) for backpack in backpacks if backpack]
    sum_of_priorities = sum(prioritize(item) for item in misplaced_items)
    print(f"Part 1 answer: {sum_of_priorities}")
    group_badges = [identify_group(backpacks[idx], backpacks[idx+1], backpacks[idx+2])
                    for idx in range(0, len(backpacks)-1, 3)]
    sum_of_group_priorities = sum(prioritize(badge) for badge in group_badges)
    print(f"Part 2 answer: {sum_of_group_priorities}")
    