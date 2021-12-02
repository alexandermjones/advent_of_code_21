# Script for day 2 of advent of code 2021

class Submarine():
    """
    A submarine with a list of instructions for movement and its position.
    """
    def __init__(self, commands: list):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0
        self.commands = commands


    def reset_position(self):
        """
        Reset the submarine's position to be 0 everywhere.
        """
        self.horizontal = 0
        self.depth = 0
        self.aim = 0


    def calc_new_position(self, command: str):
        """
        Calculate the new horizontal and vertical position based on an input instruction.
        """
        if "forward" in command:
            self.horizontal += int(command.strip("forward "))
            self.depth += (self.aim * int(command.strip("forward ")))
        elif "down" in command:
            self.aim += int(command.strip("down "))
        elif "up" in command:
            self.aim -= int(command.strip("up "))
        else:
            raise ValueError("Command should contain 'forward', 'down' or 'up'.")


    def calc_final_value(self, part):
        """
        Calculate the final value of the submarine depending on instruction set (part).
        """
        self.reset_position()
        for command in self.commands: self.calc_new_position(command)
        if part == 1:
            return self.horizontal * self.aim
        elif part == 2:
            return self.horizontal * self.depth
        else:
            raise ValueError("Part should be either 1 or 2.")


# Test class works on the test data provided
test_data = ["forward 5",
             "down 5",
             "forward 8",
             "up 3",
             "down 8",
             "forward 2"
            ]
test_submarine = Submarine(test_data)
assert test_submarine.calc_final_value(1) == 150
assert test_submarine.calc_final_value(2) == 900

# Open puzzle input
with open("2_input.txt") as f:
    str_input = f.readlines()

submarine = Submarine(str_input)
print(f"Answer to day 2, part 1 is: {submarine.calc_final_value(1)}")
print(f"Answer to day 2, part 2 is: {submarine.calc_final_value(2)}")