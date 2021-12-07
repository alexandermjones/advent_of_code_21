# Script for day 6 of advent of code 2021

def calc_num_lanternfish(str_input: str, num_days: int) -> int:
    """
    Calculate the number of lanternfish after num_days given the str_input.

    Creates a dictionary with keys as fish times and values as the number of fish who have that time.
    This is updated each day and the final number of lanternfish is sum of all dictionary values.
    """
    lanternfish_times = [int(x) for x in str_input.split(",")]
    lanternfish_dict = {x: 0 for x in range(0, 9)}
    for fish_time in lanternfish_times: lanternfish_dict[fish_time] += 1
    for _ in range(num_days):
        lanternfish_dict = update_lanternfish_times(lanternfish_dict)
    num_lanternfish = sum(lanternfish_dict.values())
    return num_lanternfish


def update_lanternfish_times(lanternfish_dict: dict) -> dict:
    """
    Update the lanternfish_dict for a single day.
    
    Set the new key total for a day to be the value for the previous day,
    but add the value for old 0-fish to the value for 6-fish and create new 8-fish.
    """
    updated_lanternfish_dict = {x: 0 for x in range(0, 9)}
    for key in lanternfish_dict.keys():
        if key > 0:
            updated_lanternfish_dict[key - 1] += lanternfish_dict[key]
        else:
            updated_lanternfish_dict[6] += lanternfish_dict[key]
            updated_lanternfish_dict[8] += lanternfish_dict[key]
    return updated_lanternfish_dict


# Test functions work on the test data provided
test_data = "3,4,3,1,2"
assert calc_num_lanternfish(test_data, 80) == 5934
assert calc_num_lanternfish(test_data, 256) == 26984457539

# Open puzzle input
with open("input_data/6_input.txt") as f:
    str_input = f.read()

print(f"Answer to day 6, part 1 is: {calc_num_lanternfish(str_input, 80)}")
print(f"Answer to day 6, part 2 is: {calc_num_lanternfish(str_input, 256)}")