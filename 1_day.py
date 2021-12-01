# Script for day 1 of advent of code 2021

def count_increases(input: list):
    count = 0
    for i in range(1, len(input)):
        if int(input[i]) > int(input[i-1]):
            count += 1
    return count


def create_sliding_windows(input: list):
    windows = []
    for i in range(2, len(input)):
        window = int(input[i-2]) + int(input[i-1]) + int(input[i])
        windows.append(window)
    return windows


with open("1_input.txt") as f:
    input = f.readlines()

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

print(count_increases(input))
print(count_increases(create_sliding_windows(input)))