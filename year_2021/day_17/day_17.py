import numpy as np
import os
import datetime

curr_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(curr_dir, "puzzle_input_day_17.txt")

with open(input_path, "r") as f:
    puzzle_input = f.readlines()[0]

x_part = puzzle_input.split(':')[1].split(',')[0].split('=')[1]
x_min = int(x_part.split('..')[0])
x_max = int(x_part.split('..')[1])
y_part = puzzle_input.split(':')[1].split(',')[1].split('=')[1]
y_min = int(y_part.split('..')[0])
y_max = int(y_part.split('..')[1])

hit_set = set()
highest_height = 0

for x_velocity_init in range(1,x_max+1):
    for y_velocity_init in range(y_min, 4*abs(y_min)):
        x_pos = 0
        x_velocity = x_velocity_init
        y_pos = 0
        y_velocity = y_velocity_init
        max_height = y_pos

        while (y_pos >= y_min) and (x_pos <= x_max):
            x_pos += x_velocity
            y_pos += y_velocity
            max_height = max(max_height, y_pos)

            if (y_min <= y_pos <= y_max) and (x_min <= x_pos <= x_max):
                highest_height = max(highest_height, max_height)
                hit_set.add((x_velocity_init, y_velocity_init))

            x_velocity = max(0, x_velocity - 1)
            y_velocity -= 1

print(f"Part 1: {int(highest_height)}")
print(f"Part 2: {len(hit_set)}")
