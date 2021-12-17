import numpy as np
import os
import datetime

curr_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(curr_dir, "puzzle_input_day_17.txt")

with open(input_path, "r") as f:
    puzzle_input = f.readlines()[0]

print(puzzle_input)
x_part = puzzle_input.split(':')[1].split(',')[0].split('=')[1]
x_min = int(x_part.split('..')[0])
x_max = int(x_part.split('..')[1])
y_part = puzzle_input.split(':')[1].split(',')[1].split('=')[1]
y_min = int(y_part.split('..')[0])
y_max = int(y_part.split('..')[1])

print(x_min, x_max, y_min, y_max)

highest_y_velocity_hit = 0

for y_velocity_init in range(1, 4*abs(y_min)):
    y_step = 0
    y_velocity = y_velocity_init
    timesteps = 0

    while y_step >= y_min:
        y_step += y_velocity
        y_velocity -= 1
        timesteps += 1

        if y_min <= y_step <= y_max:
            print(f"Y hit! Position: {y_step}, initial velocity: {y_velocity_init}")

            x_velocity = 1

            while True:
                x_pos = x_velocity * (x_velocity - 1)
                if x_pos < x_min:
                    x_velocity += 1
                elif x_min <= x_pos <= x_max:
                    print(f"Complete hit! Position: {x_pos}, {y_step}, initial velocity: {y_velocity_init}")
                    print(f"Greatest height: {y_velocity_init * (y_velocity_init +1)/2}")
                    break
                elif x_pos > x_max:
                    break