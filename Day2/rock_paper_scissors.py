"""Advent of Code 2022 - Day 2 Solution"""
INPUT_FILE = r"Day2\input.txt"

def load_input(file_path: str) -> list:
    """Loads input data from txt file

    Args:
        input_file (str): file name

    Returns:
        list: list of file contents line by line
    """
    with open(file_path, mode='r', encoding="UTF-8") as file:
        return file.read().split('\n')
    
def play_rps(strategy:list) -> int:
    """Calculates total score for playing rock-paper-scissors tournament  with given strategy

    Args:
        strategy (list): strategy to play tournament

    Returns:
        int: total score
    """
    total_score = 0
    for play in strategy:
        if play:
            oponents_play, your_play = play.split(' ')
            total_score += points_for_play(compare_play(oponents_play, your_play), your_play)
    return total_score

def compare_play(oponents_play: str, your_play: str) -> int:
    """Finds winner of current play

    Args:
        oponents_play (str): what opponent played
        your_play (str): what you played

    Returns:
        int: result in form:
                -1 - lose
                 0 - tie
                 1 - win
    """
    match oponents_play:
        case 'A': # rock
            match your_play:
                case 'X': return 0 # rock
                case 'Y': return 1 # paper
                case 'Z': return -1 # scissors
        case 'B': # paper
            match your_play:
                case 'X': return -1
                case 'Y': return 0
                case 'Z': return 1
        case 'C': # scissors
            match your_play:
                case 'X': return 1
                case 'Y': return -1
                case 'Z': return 0


def points_for_play(result: int, your_play: str) -> int:
    """Calculates score for given play

    Args:
        result (int): result of compare_play()
        your_play (str): what you played

    Returns:
        int: score
    """
    score = 0
    match your_play:
        case 'X': score += 1
        case 'Y': score += 2
        case 'Z': score += 3

    match result:
        case -1: score += 0
        case 0: score += 3
        case 1: score += 6

    return score

def predict_strategy(strategy: list) -> list:
    """Changes input for second strategy plan

    Args:
        strategy (list): previous strategy list

    Returns:
        list: new strategy list
    """
    predicted_strategy = [play[:2] for play in strategy if play]
    for idx, play in enumerate(strategy):
        if play:
            oponents_play, expected_result = play.split(' ')
            match expected_result:
                case 'X': # lose
                    match oponents_play:
                        case 'A': predicted_strategy[idx] += 'Z'
                        case 'B': predicted_strategy[idx] += 'X'
                        case 'C': predicted_strategy[idx] += 'Y'
                case 'Y': # tie
                    match oponents_play:
                        case 'A': predicted_strategy[idx] += 'X'
                        case 'B': predicted_strategy[idx] += 'Y'
                        case 'C': predicted_strategy[idx] += 'Z'
                case 'Z': # win
                    match oponents_play:
                        case 'A': predicted_strategy[idx] += 'Y'
                        case 'B': predicted_strategy[idx] += 'Z'
                        case 'C': predicted_strategy[idx] += 'X'
    return predicted_strategy

if __name__ == '__main__':
    strategy_list = load_input(INPUT_FILE)
    print(f"Part 1 answer: {play_rps(strategy_list)}")
    print(f"Part 2 answer: {play_rps(predict_strategy(strategy_list))}")
    