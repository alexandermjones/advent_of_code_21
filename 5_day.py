# Script for day 5 of advent of code 2021

def find_danger_points_of_line(line: str, part_one: True) -> list:
    """
    Find the danger points (points the line crosses over) from the string input of the line.
    """
    coords = line.split(" -> ")
    x1 = int(coords[0].split(",")[0])
    y1 = int(coords[0].split(",")[1])
    x2 = int(coords[1].split(",")[0])
    y2 = int(coords[1].split(",")[1])
    # For part one we only consider straight lines
    if part_one and x1 != x2 and y1 != y2:
        return []
    if x1 == x2:
        y1, y2 = min(y1, y2), max(y1, y2)
        danger_points = [(x1,y) for y in list(range(y1, y2+1))]
    elif y1 == y2:
        x1, x2 = min(x1, x2), max(x1, x2)
        danger_points = [(x,y1) for x in list(range(x1, x2+1))]
    else:
        if x1 < x2:
            x_danger_points = list(range(x1, x2+1))
        else:
            x_danger_points = list(range(x1, x2-1, -1))
        if y1 < y2:
            y_danger_points = list(range(y1, y2+1))
        else:
            y_danger_points = list(range(y1, y2-1, -1))
        danger_points = list(zip(x_danger_points, y_danger_points))
    return danger_points


def find_number_of_danger_points(str_input: list, part_one: bool) -> int:
    """
    Find the total number of points at which lines are intersecting.
    """
    danger_points = {"one": set(), "multiple": set()}
    for line in str_input:
        danger_points_of_line = find_danger_points_of_line(line, part_one)
        for point in danger_points_of_line:
            if point in danger_points["multiple"]:
                continue
            elif point in danger_points["one"]:
                danger_points["multiple"].add(point)
                danger_points["one"].remove(point)
            else:
                danger_points["one"].add(point)
    number_danger_points = len(danger_points["multiple"])
    return number_danger_points


# Test functions work on the test data provided
with open("test_data/5_test.txt") as f:
    test_data = f.readlines()
assert find_number_of_danger_points(test_data, True) == 5
assert find_number_of_danger_points(test_data, False) == 12

# Open puzzle input
with open("input_data/5_input.txt") as f:
    str_input = f.readlines()

print(f"Answer to day 5, part 1 is: {find_number_of_danger_points(str_input, True)}")
print(f"Answer to day 5, part 2 is: {find_number_of_danger_points(str_input, False)}")