# Script for day 4 of advent of code 2021

class BingoBoard():
    """
    A class for a 5x5 (understood as a list of integers) bingo board.
    """
    def __init__(self, board_input: str):
        """
        Given the board input, convert this to the board list - a list of tuples of the 
        numbers in the board_input and a bool determining whether it has been called or not.
        """
        self.board = [(int(x), False) for x in board_input]


    def update_board(self, number_called: int):
        """
        Update the board after a number is called to set it as true if it's in the board.
        """
        self.board = list(map(lambda x: (x[0], True) if x[0] == number_called else x, self.board))


    def check_win(self):
        """
        Check whether we have a winning row or column in the board.
        """
        for i in range(0, 5):
            # Check whether we have a complete row
            if all([x[1] for x in self.board[i*5 : i*5+5]]):
                return True
            # Create our column and then check whether it is complete
            column = [self.board[x*5 + i] for x in range(5)]
            if all((x[1] for x in column)):
                return True
        return False


    def calc_score(self, number_called: int):
        """
        Calculate the score of the board according the scoring rules.
        """
        sum_unmarked_numbers = sum([x[0] for x in self.board if not x[1]])
        score = sum_unmarked_numbers * number_called
        return score


    def calc_when_won(self, numbers_called):
        """
        Calculate the point at which a board wins and its score when it has.
        """
        for i, number_called in enumerate(numbers_called):
            self.update_board(number_called)
            if self.check_win():
                return i, self.calc_score(number_called)


def process_input(str_input: list) -> tuple:
    """
    Process the input into a list of the boards_input and the numbers to call.
    """
    boards_input = []
    for line_number in range(len(str_input)):
        if line_number == 0:
            numbers_called = [int(x) for x in str_input[line_number].split(",")]
        # First lines of each bingo board are 2 modulo 6
        elif line_number % 6 == 2:
            elements_of_interest = [str_input[x].split() for x in range(line_number, line_number+5)]
            board_input = sum(elements_of_interest, [])
            boards_input.append(board_input)
    return boards_input, numbers_called


def create_and_process_boards(boards_input, numbers_called) -> list:
    """
    Create each board and calculate when it wins and its score.
    """
    board_win_time_and_scores = []
    for board_input in boards_input:
        board = BingoBoard(board_input)
        win_time, score = board.calc_when_won(numbers_called)
        board_win_time_and_scores.append((win_time, score))
    return board_win_time_and_scores


def calc_winning_board_score(board_win_time_and_scores, part_one: bool):
    """
    Calculate which board wins first (part_one) or last (part_two = not part_one)
    and return its score.
    """
    if part_one:
        win_time = min([x[0] for x in board_win_time_and_scores])
    else:
        win_time = max([x[0] for x in board_win_time_and_scores])
    winning_score = [x[1] for x in board_win_time_and_scores if x[0] == win_time][0]
    return winning_score


def calc_final_score(str_input, part_one: bool) -> int:
    """
    Given the input, return the solution to part_one or part_two (not part_one).
    """
    boards_input, numbers_called = process_input(str_input)
    board_win_time_and_scores = create_and_process_boards(boards_input, numbers_called)
    winning_score = calc_winning_board_score(board_win_time_and_scores, part_one)
    return winning_score


# Test functions work on the test data provided
with open("test_data/4_test.txt") as f:
    test_data = f.readlines()
assert calc_final_score(test_data, True) == 4512
assert calc_final_score(test_data, False) == 1924

# Open puzzle input
with open("input_data/4_input.txt") as f:
    str_input = f.readlines()

print(f"Answer to day 4, part 1 is: {calc_final_score(str_input, True)}")
print(f"Answer to day 4, part 2 is: {calc_final_score(str_input, False)}")