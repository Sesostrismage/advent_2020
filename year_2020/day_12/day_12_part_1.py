import numpy as np
import os
import pandas as pd

curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "data.txt"))
# f = open(os.path.join(curr_dir, "test.txt"))
txt = f.readlines()
f.close()

txt_cleaned = [item.strip() for item in txt]

turn_list = ["E", "S", "W", "N"]

lon = 0
lat = 0


def turn(curr_heading, turn_direction, val):
    if turn_direction == "R":
        steps = int(val / 90)
    elif turn_direction == "L":
        steps = -int(val / 90)
    curr_heading_idx = turn_list.index(curr_heading)
    new_heading_idx = (curr_heading_idx + steps) % 4
    new_heading = turn_list[new_heading_idx]

    return new_heading


def move_abs(direction, speed, pos_list):
    if direction == "N":
        ew_pos_new = pos_list[0]
        ns_pos_new = pos_list[1] + speed
    elif direction == "E":
        ew_pos_new = pos_list[0] + speed
        ns_pos_new = pos_list[1]
    elif direction == "S":
        ew_pos_new = pos_list[0]
        ns_pos_new = pos_list[1] - speed
    elif direction == "W":
        ew_pos_new = pos_list[0] - speed
        ns_pos_new = pos_list[1]

    return [ew_pos_new, ns_pos_new]


def move_rel(vessel_heading, speed, pos_list):
    if vessel_heading == "N":
        ew_pos_new = pos_list[0]
        ns_pos_new = pos_list[1] + speed
    elif vessel_heading == "E":
        ew_pos_new = pos_list[0] + speed
        ns_pos_new = pos_list[1]
    elif vessel_heading == "S":
        ew_pos_new = pos_list[0]
        ns_pos_new = pos_list[1] - speed
    elif vessel_heading == "W":
        ew_pos_new = pos_list[0] - speed
        ns_pos_new = pos_list[1]

    return [ew_pos_new, ns_pos_new]


heading = "E"
pos = [0, 0]

for instruction in txt_cleaned:
    part1 = instruction[0]
    part2 = int(instruction[1:])

    if part1 in ["L", "R"]:
        heading = turn(heading, part1, part2)

    elif part1 in ["N", "E", "S", "W"]:
        pos = move_abs(part1, part2, pos)

    elif part1 in ["F"]:
        pos = move_rel(heading, part2, pos)

print(f"Manhattan distance: {abs(pos[0]) + abs(pos[1])}")
