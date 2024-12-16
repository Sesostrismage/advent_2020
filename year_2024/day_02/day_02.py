import copy
from pathlib import Path

import pandas as pd


def check_levels(l):
    diff = l[1] - l[0]
    if diff > 0:
        sign = 1
        safe = True
    elif diff < 0:
        sign = -1
        safe = True
    else:
        sign = 0
        safe = False

    if safe:
        for idx in range(1, len(l)):
            diff = l[idx] - l[idx - 1]
            step = sign * diff

            if (step < 1) or (step > 3):
                safe = False
                break

    return safe


def remove_check_levels(l):
    safe = check_levels(l)

    if not safe:
        for i in range(len(l)):
            cropped_list = copy.deepcopy(l)
            cropped_list.pop(i)
            safe = check_levels(cropped_list)

            if safe:
                break

    return safe


curr_dir = Path(__file__).parent
input_path = curr_dir / "puzzle_input_day_02.txt"

with open(input_path, "r") as f:
    text = f.read()

safe_count = 0

for line in text.splitlines():
    line_split = line.split(" ")
    line_int = [int(item) for item in line_split]
    safe = check_levels(line_int)

    if safe:
        safe_count += 1

print(f"Part 1: {safe_count}")

safe_count = 0

for line in text.splitlines():
    direction = None
    skip = False
    line_split = line.split(" ")
    line_int = [int(item) for item in line_split]
    safe = remove_check_levels(line_int)

    if safe:
        safe_count += 1


print(f"Part 2: {safe_count}")
