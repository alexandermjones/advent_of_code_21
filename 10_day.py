# Script for day 10 of advent of code 2021

# The matching symbols for closing a chunk
CLOSING_SYMBOLS = {'(': ')',
                   '[': ']',
                   '{': '}',
                   '<': '>'}
# The score of a corrupted character
CORRUPTED_CHARACTER_SCORE = {')': 3,
                             ']': 57,
                             '}': 1197,
                             '>': 25137,
                             '\n' : 0}
# The score of a completed character
COMPLETED_CHARACTER_SCORE = {')': 1,
                             ']': 2,
                             '}': 3,
                             '>': 4}


def find_line_error(line: str) -> tuple:
    """
    Find the error in the line.
    
    Find either the bad character, or the characters that need closing
    and True if corrupted or False if not corrupted (incomplete).
    """
    characters_to_close = []
    for i, character in enumerate(line):
        if character in CLOSING_SYMBOLS.keys():
            characters_to_close.append(character)
        elif character == CLOSING_SYMBOLS[characters_to_close[-1]]:
            del(characters_to_close[-1])
        elif character == '\n':
            return characters_to_close, False
        else:
            return character, True
    return characters_to_close, False


def calculate_total_error_score(str_input: list) -> int:
    """
    Calculate the total error score for part one.
    """
    total_syntax_error_score = 0
    for line in str_input:
        character, corrupted = find_line_error(line)
        total_syntax_error_score += CORRUPTED_CHARACTER_SCORE[character] if corrupted else 0
    return total_syntax_error_score


def calculate_middle_completion_score(str_input: list) -> int:
    """
    Calculate the middle completion score for part two.
    """
    completion_string_scores = []
    for line in str_input:
        characters_to_close, corrupted = find_line_error(line)
        if not corrupted:
            characters_to_close.reverse()
            completion_string_score = 0
            for character in characters_to_close:
                completion_string_score = completion_string_score*5 + COMPLETED_CHARACTER_SCORE[CLOSING_SYMBOLS[character]]
            completion_string_scores.append(completion_string_score)
    completion_string_scores.sort()
    return completion_string_scores[int((len(completion_string_scores)+1)/2) - 1]


# Test functions work on the test data provided
with open("test_data/10_test.txt") as f:
    test_data = f.readlines()

assert calculate_total_error_score(test_data) == 26397
assert calculate_middle_completion_score(test_data) == 288957

# Open puzzle input
with open("input_data/10_input.txt") as f:
    str_input = f.readlines()

print(f"Answer to day 9, part 1 is: {calculate_total_error_score(str_input)}")
print(f"Answer to day 7, part 2 is: {calculate_middle_completion_score(str_input)}")