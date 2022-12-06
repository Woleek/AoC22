"""Advent of Code 2022 - Day 5 Solution"""
INPUT_FILE = "Day6/input.txt"


def load_input(file_path: str) -> str:
    """Loads input data from txt file

    Args:
        input_file (str): file name

    Returns:
        list: list of file contents line by line
    """
    with open(file_path, mode='r', encoding="UTF-8") as file:
        return file.read().rstrip()


def detect_start_packet_marker(datastream: str) -> int:
    """Detects start of packet marker - 4 distinct characters

    Args:
        datastream (str): input datastream of characters

    Returns:
        int: number of characters processed before marker was found
    """
    num_proc = None
    for idx in range(3, len(datastream)):
        if len(set(datastream[idx-3: idx+1])) == 4:
            num_proc = idx+1
            break
    return num_proc


def detect_start_message_marker(datastream: str) -> int:
    """Detects start of message marker - 14 distinct characters

    Args:
        datastream (str): input datastream of characters

    Returns:
        int: number of characters processed before marker was found
    """
    num_proc = None
    for idx in range(13, len(datastream)):
        if len(set(datastream[idx-13: idx+1])) == 14:
            num_proc = idx+1
            break
    return num_proc


if __name__ == '__main__':
    input_stream = load_input(INPUT_FILE)
    print(f"Part 1 answer: {detect_start_packet_marker(input_stream)}")
    print(f"Part 2 answer: {detect_start_message_marker(input_stream)}")
