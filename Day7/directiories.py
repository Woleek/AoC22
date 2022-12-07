"""Advent of Code 2022 - Day 7 Solution"""
import re
from math import inf

INPUT_FILE = "Day7/input.txt"
current_path = '/'
dir_tree = {}
result1 = 0
result2 = inf


def load_input(file_path: str) -> list:
    """Loads input data from txt file

    Args:
        input_file (str): file name

    Returns:
        list: list of file contents line by line
    """
    with open(file_path, mode='r', encoding="UTF-8") as file:
        return file.read().rstrip().split('\n')


def go_to_outermost():
    """Changes current_path to outermost directory
    """
    global current_path
    current_path = '/'


def go_out():
    """Changes current_path to one directory up
    """
    global current_path
    idx = current_path.rfind('/')
    current_path = current_path[: idx]


def go_in(direct: str):
    """Changes current_path to given directory down

    Args:
        direct (str): directory to change to
    """
    global current_path
    if current_path == '/':
        current_path += direct
    else:
        current_path += '/' + direct


def execute_command(command: str):
    """Executes given command

    Args:
        command (str): line of command
    """
    if re.match('cd', command):
        direct = command[3:]
        match direct:
            case '/':
                go_to_outermost()
            case '..':
                go_out()
            case _:
                go_in(direct)


def create_new(name: str, size: int=None):
    """Creates new file or directory in current_path

    Args:
        name (str): name of file/dir to create
        size (int, optional): size of new file. Defaults to None when dir is being created.
    """
    global dir_tree
    subdirs = current_path.split('/')[1:]
    if not subdirs[0] and not size:
        dir_tree[name] = {}
    elif not subdirs[0] and size:
        dir_tree[name] = size
    else:
        dest_dir = 'dir_tree'
        for subdir in subdirs:
            dest_dir += f"['{subdir}']"
        if size:
            exec(dest_dir + f"['{name}'] = {size}")
        else:
            exec(dest_dir + f"['{name}']" + ' = {}')


def process_output(line: str):
    """Process terminal output that was not a command

    Args:
        line (str): terminal output line
    """
    if re.match('dir', line):
        name = line[4:]
        create_new(name)
    else:
        size, name = line.split(' ')
        create_new(name, size)


def build_dir_tree(terminal_output: list):
    """Builds directory tree from terminal output

    Args:
        terminal_output (list): list of commands lines from output
    """
    for line in terminal_output:
        if line[0] == '$':
            execute_command(line[2:])
        else:
            process_output(line)


def find_small_space(node: dict=dir_tree) -> int:
    """Recursion over all directories and its files.
    Finds all directories of size <= 100000 and calculates sum of their sizes as result1

    Args:
        node (dict, optional): current directory being searched. Defaults to dir_tree as outermost one.

    Returns:
        int: size of current directory
    """
    global result1
    temp_res = 0
    for value in node.values():
        if isinstance(value, dict):
            temp_res += find_small_space(value)
        else:
            temp_res += int(value)
    if temp_res <= 100000:
        result1 += temp_res
    return temp_res


def find_del_space(node: dict=dir_tree) -> int:
    """Recursion over all directories and its files.
    Finds smallest direcory that has at least space_needed size and sets it as result2

    Args:
        node (dict, optional): current directory being searched. Defaults to dir_tree as outermost one.

    Returns:
        int: size of current directory
    """
    global result2
    temp_res = 0
    for value in node.values():
        if isinstance(value, dict):
            temp_res += find_del_space(value)
        else:
            temp_res += int(value)
    if temp_res >= space_needed and temp_res < result2:
        result2 = temp_res
    return temp_res

if __name__ == '__main__':
    input_lines = load_input(INPUT_FILE)
    build_dir_tree(input_lines)
    full_disk_space = find_small_space()
    space_needed = 30000000 - (70000000 - full_disk_space)
    find_del_space()
    print(f"Part 1 answer: {result1}")
    print(f"Part 2 answer: {result2}")
