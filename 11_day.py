# Script for day 11 of advent of code 2021

def create_starting_grid(str_input) -> list:
    """
    """
    grid = []
    for line in str_input:
        grid.extend([int(x) for x in line])
    return grid


def process_step(grid: list) -> list:
    """
    """
    flashes = 0
    for position, octopus_energy in enumerate(grid):
        octopus_energy += 1
        if octopus_energy == 9:
            flashes += 1


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