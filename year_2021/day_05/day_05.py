import os
import timeit

import numpy as np

start = timeit.timeit()


curr_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(curr_dir, "puzzle_input_day_05.txt")

with open(input_path, "r") as f:
    puzzle_input = f.readlines()

line_list = []
x_max = 0
y_max = 0

for line in puzzle_input:
    line_dict = {
        "x0": int(line.split("->")[0].split(",")[0]),
        "y0": int(line.split("->")[0].split(",")[1]),
        "x1": int(line.split("->")[1].split(",")[0]),
        "y1": int(line.split("->")[1].split(",")[1]),
    }
    x_max = max([x_max, line_dict["x0"], line_dict["x1"]])
    y_max = max([y_max, line_dict["y0"], line_dict["y1"]])
    line_list.append(line_dict)


# Part 1.
array = np.zeros([x_max + 1, y_max + 1])

for line_dict in line_list:
    x0 = line_dict["x0"]
    x1 = line_dict["x1"]
    y0 = line_dict["y0"]
    y1 = line_dict["y1"]

    if x0 == x1:
        if y0 < y1:
            array[x0, y0 : y1 + 1] += 1
        else:
            array[x0, y1 : y0 + 1] += 1

    elif y0 == y1:
        if x0 < x1:
            array[x0 : x1 + 1, y0] += 1
        else:
            array[x1 : x0 + 1, y0] += 1

print(f"Part 1: {len(array[array > 1])}")


# Part 2.
array = np.zeros([x_max + 1, y_max + 1])

for line_dict in line_list:
    x0 = line_dict["x0"]
    x1 = line_dict["x1"]
    y0 = line_dict["y0"]
    y1 = line_dict["y1"]

    if x0 == x1:
        if y0 < y1:
            array[x0, y0 : y1 + 1] += 1
        else:
            array[x0, y1 : y0 + 1] += 1

    elif y0 == y1:
        if x0 < x1:
            array[x0 : x1 + 1, y0] += 1
        else:
            array[x1 : x0 + 1, y0] += 1

    else:
        i = x0
        i_end = x1
        if x0 < x1:
            sign_x = 1
        else:
            sign_x = -1

        j = y0
        if y0 < y1:
            sign_y = 1
        else:
            sign_y = -1

        while i != i_end + sign_x:
            array[i, j] += 1
            i += sign_x
            j += sign_y

print(f"Part 2: {len(array[array > 1])}")

print(f"Time: {timeit.timeit() - start}")
