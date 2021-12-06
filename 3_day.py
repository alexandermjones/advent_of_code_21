# Script for day 3 of advent of code 2021

def get_most_common_bit_at_n(binary_strs: list, n: int) -> str:
    """
    Get the most common bit at the nth position across all binary strings given.
    """
    bit_set = [binary_str[n] for binary_str in binary_strs]
    # Number of 1s is >= number of 0s iff number of 1s >= len(bits) - num_ones.
    # Part 2 specifies that when we have an equal number, we should return 1.
    return "1" if 2*bit_set.count("1") >= len(bit_set) else "0"


def calc_most_and_least_common_bits(binary_strs: list) -> tuple:
    """
    Provide the strings of the most and least common bits for each index in the binary strings given.
    """
    number_chars = len(binary_strs[0]) - 1
    most_common_bits_list = [get_most_common_bit_at_n(binary_strs, n) for n in range(number_chars)]
    most_common_bits = "".join(most_common_bits_list)
    # Least common bits is complement of most common - we replace 1s with 0s and 0s with 1s.
    least_common_bits = most_common_bits.replace("1", "2").replace("0", "1").replace("2", "0")
    return most_common_bits, least_common_bits


def calc_power_consumption(binary_strs: list):
    """
    Calculate the power consumption of the submarine (answer to part one).

    The power consumption is the most common bits * least common bits.
    """
    most_common_bits, least_common_bits = calc_most_and_least_common_bits(binary_strs)
    gamma_rate = int(most_common_bits, base=2)
    epsilon_rate = int(least_common_bits, base=2)
    power_consumption = gamma_rate * epsilon_rate
    return power_consumption


def bit_criteria_at_n(binary_strs: list, n: int, ogr: bool) -> list:
    """
    Follow the bit criteria algorithm at an index n.

    This function returns only the binary strings which match the most (ogr) or least (!ogr, i.e. co2)
    common bit at index n.
    """
    # Oxygen generator rating uses most common bit, else we wants least common bit (its complement)
    if ogr:
        bit_to_keep_at_n = get_most_common_bit_at_n(binary_strs, n)
    else:
        bit_to_keep_at_n = get_most_common_bit_at_n(binary_strs, n).replace("1", "2").replace("0", "1").replace("2", "0")
    binary_strs_reduced = [binary_str for binary_str in binary_strs if binary_str[n] == bit_to_keep_at_n]
    return binary_strs_reduced


def bit_criteria_algorithm(binary_strs: list, ogr: bool) -> str:
    """
    Follow the bit criteria algorithm for ogr or co2 (!ogr).

    This function returns a single string once the algorithm has finished,
    or raises a warning if this does not terminate (bad input).
    """
    number_chars = len(binary_strs[0]) - 1
    binary_strs_copy = binary_strs
    for n in range(number_chars):
        binary_strs_copy = bit_criteria_at_n(binary_strs_copy, n, ogr)
        if len(binary_strs_copy) == 1:
            return binary_strs_copy[0]
    raise RuntimeWarning("Bit criteria algorithm did not terminate.")


def calc_life_support_rating(binary_strs: list):
    """
    Calculate the life support rating of the submarine (answer to part 2).

    The life support rating is the bit criteria algorithm for ogr * bit criteria algorithm
    for co2 (!ogr).
    """
    oxygen_binary_str = bit_criteria_algorithm(binary_strs, True)
    co2_binary_str = bit_criteria_algorithm(binary_strs, False)
    oxygen_generator_rating = int(oxygen_binary_str, base=2)
    co2_scrubber_rating = int(co2_binary_str, base=2)
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating
    return life_support_rating


# Test functions work on the test data provided
with open("3_test.txt") as f:
    test_data = f.readlines()
assert calc_power_consumption(test_data) == 198
assert calc_life_support_rating(test_data) == 230

# Open puzzle input
with open("3_input.txt") as f:
    binary_strs = f.readlines()

print(f"Answer to day 3, part 1 is: {calc_power_consumption(binary_strs)}")
print(f"Answer to day 3, part 2 is: {calc_life_support_rating(binary_strs)}")