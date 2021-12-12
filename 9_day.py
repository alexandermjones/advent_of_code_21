# Script for day 9 of advent of code 2021

def find_low_points(heightmap: list) -> list:
    """
    Find all the low points in the heatmap.

    Return a list of a tuple of low points and their positions (x and y).
    Iterates through each point and breaks out the iteration if it is outside the heatmap or
    greater than a point above or below it.
    """
    low_points = []
    for line_number, line in enumerate(heightmap):
        for position, number in enumerate(line):
            if position > 0 and number >= line[position-1]:
                continue
            elif position < len(line) - 1 and number >= line[position+1]:
                continue
            elif line_number > 0 and number >= heightmap[line_number - 1][position]:
                continue
            elif line_number < len(heightmap) - 1 and number >= heightmap[line_number + 1][position]:
                continue
            low_point_position = position, line_number
            low_points.append((number, low_point_position))
    return low_points


def calc_overall_risk_level(str_input: list) -> int:
    """
    Calculate the risk level of each lowpoint from the heatmap and returns the overall risk level.

    This is the answer to part one.
    """
    heightmap = [[int(x.strip()) for x in line if x.strip()] for line in str_input]
    low_points = find_low_points(heightmap)
    return sum([x[0] + 1 for x in low_points])


def find_point_neighbours_in_basin(heightmap: list, point_position: tuple, line_length, height_length) -> set:
    """
    Given a point_position in the heightmap, return all neighbours in the basin.

    Calculate all point_neighbours possible, then removes all those which are outside the heightmap or a 9.
    Returns these point_neighbours as a list of tuples of x and y coordinates.
    """
    point_neighbours = {(point_position[0] - 1, point_position[1]), 
                        (point_position[0] + 1, point_position[1]),
                        (point_position[0], point_position[1] - 1),
                        (point_position[0], point_position[1] + 1)}
    point_neighbours = {position for position in point_neighbours if 0 <= position[0] <= line_length - 1}
    point_neighbours = {position for position in point_neighbours if 0 <= position[1] <= height_length - 1}
    point_neighbours = {position for position in point_neighbours if heightmap[position[1]][position[0]] < 9}
    return point_neighbours


def calc_largest_basin_sizes(str_input: list) -> int:
    """
    Calculate the largest basin sizes and returns this (answer to part 2).

    Iterates through each low point position and calculates its basin as a set.
    Creates a set of each of these basins, then calculates the largest three and returns
    the product of these sizes.
    """
    heightmap = [[int(x.strip()) for x in line if x.strip()] for line in str_input]
    line_length = len(heightmap[0])
    height_length = len(heightmap)
    low_points = find_low_points(heightmap)
    basins = set()
    for _, low_point_position in low_points:
        basin = set((low_point_position, ))
        basin_has_grown = True
        while basin_has_grown:
            old_size = len(basin)
            basin_update = set()
            for point in basin:
                basin_update.update(find_point_neighbours_in_basin(heightmap, point, line_length, height_length))
            basin.update(basin_update)
            basin_has_grown = len(basin) > old_size
        basins.add(frozenset(basin))
    three_largest_basin_sizes = sorted([len(basin) for basin in basins], reverse=True)[:3]
    return three_largest_basin_sizes[0] * three_largest_basin_sizes[1] * three_largest_basin_sizes[2]


# Test functions work on the test data provided
with open("test_data/9_test.txt") as f:
    test_data = f.readlines()

assert calc_overall_risk_level(test_data) == 15
assert calc_largest_basin_sizes(test_data) == 1134

# Open puzzle input
with open("input_data/9_input.txt") as f:
    str_input = f.readlines()

print(f"Answer to day 9, part 1 is: {calc_overall_risk_level(str_input)}")
print(f"Answer to day 7, part 2 is: {calc_largest_basin_sizes(str_input)}")