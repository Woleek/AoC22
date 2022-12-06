"""Advent of Code 2022 - Day 5 Solution"""
import re

INPUT_FILE = "Day5/input.txt"


def load_input(file_path: str) -> list:
    """Loads input data from txt file

    Args:
        input_file (str): file name

    Returns:
        list: list of file contents line by line
    """
    with open(file_path, mode='r', encoding="UTF-8") as file:
        return file.read().rstrip().split('\n')


class Stack():
    """Stack implementation
    """

    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def isEmpty(self):
        return not self._stack

    def pop(self):
        if self.isEmpty():
            return None
        return self._stack.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self._stack[-1]

    def size(self):
        return len(self._stack)

    def __str__(self):
        toString = ""
        for element in self._stack:
            toString += f"{element} "
        return toString


def init_stacks(stacks_list: list) -> list:
    """Initializes list of stacks of crates

    Args:
        stacks_list (list): stacks from input file

    Returns:
        list: list of stacks
    """
    num_stacks = int(max(list(filter(lambda l: l, stacks_list[0].split(' ')))))

    stacks_local = [Stack() for _ in range(num_stacks)]  # stacks 0 - 8
    for row in stacks_list[1:]:
        row_items = [row[idx: idx+3].strip('[]')
                     for idx in range(0, len(row), 4)]

        for idx, item in enumerate(row_items):
            if item.replace(' ', ''):
                stacks_local[idx].push(item)
    return stacks_local


def init_moves(moves_list: list) -> list:
    """Initializes list of moves to perform by crane

    Args:
        moves_list (list): moves from input file

    Returns:
        list: list of moves
    """
    moves_local = [re.findall("\d+", move) for move in moves_list]
    return moves_local


def process_input(input_list: list) -> tuple:
    """Divieds input into stacks and moves park, runs function to process them

    Args:
        input_list (list): input as list of lines

    Returns:
        tuple: stacks and moves lists
    """
    idx = input_list.index('')  # find blank space between stack and moves

    # divide file
    stacks_space = input_list[idx-1:: -1]
    stacks_list = init_stacks(stacks_space)
    moves_space = input_list[idx+1:]
    moves_list = init_moves(moves_space)
    return (stacks_list, moves_list)


def use_crane_9000():
    """Uses crane 9000 to move crates in scenerio with stack_1,
    one crate is moved at once
    """
    for move in moves:
        for _ in range(int(move[0])):
            crate = stacks_1[int(move[1])-1].pop()
            stacks_1[int(move[2])-1].push(crate)


def use_crane_9001():
    """Uses crane 9001 with leather seats to move crates in scenerio with stack_2,
    multiple crates can be moved at once
    """
    for move in moves:
        crates = []
        for _ in range(int(move[0])):
            crates.append(stacks_2[int(move[1])-1].pop())
        crates = crates[:: -1]
        for crate in crates:
            stacks_2[int(move[2])-1].push(crate)


def peek_all(stacks_to_peek: list) -> str:
    """Peek all top crates from given list of stacks

    Args:
        stacks_to_peek (list): stacks to peek

    Returns:
        str: peeked crates in order
    """
    peek_list = []
    for stack in stacks_to_peek:
        peek_list.append(stack.peek())
    peek_str = ''.join(x for x in peek_list)
    return peek_str


if __name__ == '__main__':
    input_file_list = load_input(INPUT_FILE)
    stacks_1, moves = process_input(input_file_list)
    stacks_2, moves = process_input(input_file_list)
    use_crane_9000()
    print(f"Part 1 answer: {peek_all(stacks_1)}")
    use_crane_9001()
    print(f"Part 2 answer: {peek_all(stacks_2)}")
