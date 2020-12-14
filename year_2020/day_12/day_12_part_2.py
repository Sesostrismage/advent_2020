import numpy as np
import os

curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "data.txt"))
# f = open(os.path.join(curr_dir, "test.txt"))
txt = f.readlines()
f.close()

txt_cleaned = [item.strip() for item in txt]

turn_list = ['E', 'S', 'W', 'N']

lon = 0
lat = 0

def turn(turn_direction, val, pos_v, pos_w):
    steps = int(val/90)

    for _ in range(steps):
        x_rel = pos_w[0] - pos_v[0]
        y_rel = pos_w[1] - pos_v[1]

        if turn_direction == 'R':
            pos_w = [pos_v[0] + y_rel, pos_v[1] - x_rel]
        elif turn_direction == 'L':
            pos_w = [pos_v[0] - y_rel, pos_v[1] + x_rel]

    return pos_w

def move_abs(direction, speed, pos_w):
    if direction == 'N':
        pos_x_new = pos_w[0]
        pos_y_new = pos_w[1] + speed
    elif direction == 'E':
        pos_x_new = pos_w[0] + speed
        pos_y_new = pos_w[1]
    elif direction == 'S':
        pos_x_new = pos_w[0]
        pos_y_new = pos_w[1] - speed
    elif direction == 'W':
        pos_x_new = pos_w[0] - speed
        pos_y_new = pos_w[1]

    return [pos_x_new, pos_y_new]

def move_rel(pos_v, pos_w, speed):
    x_rel = pos_w[0] - pos_v[0]
    y_rel = pos_w[1] - pos_v[1]

    for _ in range(speed):
        pos_v = [pos_v[0] + x_rel, pos_v[1] + y_rel]

    pos_w = [pos_v[0] + x_rel, pos_v[1] + y_rel]

    return pos_v, pos_w

vessel_heading = 'E'
pos_vessel = [0, 0]
pos_waypoint = [10, 1]

for instruction in txt_cleaned:
    part1 = instruction[0]
    part2 = int(instruction[1:])

    if part1 in ['L', 'R']:
        pos_waypoint = turn(part1, part2, pos_vessel, pos_waypoint)

    elif part1 in ['N', 'E', 'S', 'W']:
        pos_waypoint = move_abs(part1, part2, pos_waypoint)

    elif part1 in ['F']:
        pos_vessel, pos_waypoint = move_rel(pos_vessel, pos_waypoint, part2)

print(f"Manhattan distance: {abs(pos_vessel[0]) + abs(pos_vessel[1])}")
