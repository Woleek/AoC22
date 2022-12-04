"""Advent of Code 2022 - Day 4 Solution"""
INPUT_FILE = r"Day4\input.txt"


def load_input(file_path: str) -> list:
    """Loads input data from txt file

    Args:
        input_file (str): file name

    Returns:
        list: list of file contents line by line
    """
    with open(file_path, mode='r', encoding="UTF-8") as file:
        return file.read().rstrip().split('\n')


def pairs_to_sets(pairs_list: list) -> list:
    """Converts list of pairs from input to set form for further operations

    Args:
        pairs_list (list): list of pairs from input

    Returns:
        list: list of pairs
    """
    pair_sets = []
    for pair in pairs_list:
        lower_bound, upper_bound = [x.split('-') for x in pair.split(',')]
        range_to_set = lambda bounds: set(x for x in range(int(bounds[0]), int(bounds[1])+1))
        first, second = range_to_set(lower_bound), range_to_set(upper_bound)
        pair_sets.append((first, second))
    return pair_sets


def find_contained(pairs_in_sets: list) -> int:
    """Finds number of pairs where one contains the other

    Args:
        pairs_in_sets (list): list of pairs in set form

    Returns:
        int: number of contained pairs
    """
    contained = 0
    for pair in pairs_in_sets:
        first, second = pair
        if first.issubset(second) or first.issuperset(second):
            contained += 1
    return contained


def find_overlaping(pairs_in_sets: list) -> int:
    """Finds number of pairs where one overlaps the other at any point

    Args:
        pairs_in_sets (list): list of pairs in set form

    Returns:
        int: number of overlaping pairs
    """
    overlaping = 0
    for pair in pairs_in_sets:
        first, second = pair
        if not first.isdisjoint(second):
            overlaping += 1
    return overlaping


if __name__ == '__main__':
    list_of_pairs = load_input(INPUT_FILE)
    print(f"Part 1 answer: {find_contained(pairs_to_sets(list_of_pairs))}")
    print(f"Part 2 answer: {find_overlaping(pairs_to_sets(list_of_pairs))}")
