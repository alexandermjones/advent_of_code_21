# Script for day 7 of advent of code 2021

def calculate_fuel_cost(crab_locations: list, target_location: int, part_one: bool) -> int:
    """
    Calculate the amount of fuel required to move all crabs to the target_location according to
    the metric of part_one or (not part_two).
    """
    fuel = 0
    if part_one:
        for crab in crab_locations: fuel += abs(crab - target_location)
    else:
        for crab in crab_locations:
            distance_to_go = abs(crab - target_location)
            # The fuel cost is now the triangle number of distance, so we use the formula for nth triangle no.
            fuel += int((distance_to_go*(distance_to_go+1))/2)
    return fuel


def minimise_fuel(str_input: str, part_one: bool) -> tuple:
    """
    Calculate the least fuel that can be used to move all crabs to the same location according to part_one
    or part_two (not part_one).
    """
    crab_locations = [int(x) for x in str_input.split(",")]
    starting_outcome = min(crab_locations)
    final_outcome = max(crab_locations)
    # Calculate our initial fuel cost
    cheapest_fuel_cost = calculate_fuel_cost(crab_locations, starting_outcome, part_one)
    for position in range(starting_outcome+1, final_outcome+1):
        new_fuel_cost = calculate_fuel_cost(crab_locations, position, part_one)
        if new_fuel_cost < cheapest_fuel_cost:
            cheapest_fuel_cost = new_fuel_cost
    return cheapest_fuel_cost


# Test functions work on the test data provided
test_data = "16,1,2,0,4,2,7,1,2,14"
assert minimise_fuel(test_data, True) == 37
assert minimise_fuel(test_data, False) == 168

# Open puzzle input
with open("7_input.txt") as f:
    str_input = f.read()

print(f"Answer to day 7, part 1 is: {minimise_fuel(str_input, True)}")
print(f"Answer to day 7, part 2 is: {minimise_fuel(str_input, False)}")