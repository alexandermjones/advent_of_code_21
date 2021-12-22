# Script for day 18 of advent of code 2021

class SnailfishNumber():
    """
    SnailfishNumber object with rules for SnailFish arithmetic.
    """
    def __init__(self, pair: tuple):
        """
        Initialise the Snailfish number.
        """
        try:
            assert len(pair) == 2
        except AssertionError:
            raise ValueError("pair should only contain two elements",
                             f", not {len(pair}).")
        self.left = pair[0]
        self.right = pair[1]
    
    def __repr__(self):
        return (self.left, self.right)


    def __len__(self):
        if type(self.left) == int:
            left_len = 0
        else:
            left_len = len(self.left)
        if type(self.right) == int:
            right_len = 0
        else:
            right_len = len(self.right)
        return left_len + right_len + 1
    
    def __getitem__(self, key):
        raise NotImplementedError()

    
    def __add__(self):
        raise NotImplementedError()

# Test functions work on the test data provided
with open("test_data/18_test.txt") as f:
    test_data = f.readlines()

assert calculate_total_error_score(test_data) == 26397
assert calculate_middle_completion_score(test_data) == 288957

# Open puzzle input
with open("input_data/10_input.txt") as f:
    str_input = f.readlines()

print(f"Answer to day 9, part 1 is: {calculate_total_error_score(str_input)}")
print(f"Answer to day 7, part 2 is: {calculate_middle_completion_score(str_input)}")