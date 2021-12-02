import os

curr_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(curr_dir, "input_day_02.txt")

with open(input_path, "r") as f:
    puzzle_input = f.readlines()

puzzle_input = [item.strip() for item in puzzle_input]

# Part 1.
hor = 0
depth = 0

for item in puzzle_input:
    command = item.split()[0]
    amount = int(item.split()[1])

    if command == "forward":
        hor += amount
    elif command == "down":
        depth += amount
    elif command == "up":
        depth -= amount
    else:
        raise KeyError(f"Unkown command {command}")

print(f"Part 1: {hor * depth}")


# Part 2.
hor = 0
depth = 0
aim = 0

for item in puzzle_input:
    command = item.split()[0]
    amount = int(item.split()[1])

    if command == "forward":
        hor += amount
        depth += amount * aim
    elif command == "down":
        aim += amount
    elif command == "up":
        aim -= amount
    else:
        raise KeyError(f"Unkown command {command}")

print(f"Part 1: {hor * depth}")
