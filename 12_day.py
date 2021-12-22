# Script for day 12 of advent of code 2021

class Point():
    """
    Point in the cave.
    """
    def __init__(self, point: str):
        """
        """
        self.point = point
        self.large = True if point.isupper() else False


class Path():
    """
    Path between two points in the cave.
    """
    def __init__(self, first: str, second: str):
        """
        """
        if "start" in second or "end" in first:
            self.point_one = Point(second)
            self.point_two = Point(first)
        else:
            self.point_one = Point(first)
            self.point_two = Point(second)


def list_paths(str_input: str):
    """
    """
    all_single_paths = [Path(line.split("-")[0], line.split("-")[1]) for line in str_input]
    all_single_paths += [Path(line.split("-")[1], line.split("-")[0]) for line in str_input]
    all_points = {line.split("-")[0] for line in str_input}.union({line.split("-")[1] for line in str_input})
    paths = [[single_path] for single_path in all_single_paths if single_paths.point_one == "start"]


def extend_path(all_points, all_single_paths):
    """
    """
    while len(new_paths) > len(paths):
        for path in paths:
            extended_paths = [single_path for single_path in all_single_paths if single_paths.point_one == path[-1].point_two]
            extended_paths += [single_path for single_path in all_single_paths if single_paths.point_two == path[-1].point_two]



# Test functions work on the test data provided
with open("test_data/12_test_1.txt") as f:
    test_data_1 = f.readlines()
with open("test_data/12_test_2.txt") as f:
    test_data_2 = f.readlines()


assert calculate_total_error_score(test_data) == 26397
assert calculate_middle_completion_score(test_data) == 288957

# Open puzzle input
with open("input_data/12_input.txt") as f:
    str_input = f.readlines()

print(f"Answer to day 12, part 1 is: {calculate_total_error_score(str_input)}")
print(f"Answer to day 12, part 2 is: {calculate_middle_completion_score(str_input)}")