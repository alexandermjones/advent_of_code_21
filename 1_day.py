# Script for day 1 of advent of code 2021

def count_increases(input: list):
    """
    Count how many elements in the list are larger than their preceding element.
    """
    count = sum([input[i]> input[i-1] for i in range(1, len(input))])
    return count


def create_sliding_windows(input: list):
    """
    Create sliding windows of the sum of each three-tuple in a list.
    """
    windows = [input[i-2] + input[i-1] + input[i] for i in range(2, len(input))]
    return windows

# Test functions work on the test data provided
test_data = [199,
             200,
             208,
             210,
             200,
             207,
             240,
             269,
             260,
             263
            ]
assert count_increases(test_data) == 7
assert count_increases(create_sliding_windows(test_data)) == 5

# Open puzzle input
with open("input_data/1_input.txt") as f:
    str_input = f.readlines()
    int_input = [int(x) for x in str_input]

print(f"Answer to day 1, part 1 is: {count_increases(int_input)}")
print(f"Answer to day 1, part 2 is: {count_increases(create_sliding_windows(int_input))}")