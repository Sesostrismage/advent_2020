import os
import datetime

import numpy as np
import pandas as pd

start = datetime.datetime.now()

curr_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(curr_dir, "puzzle_input_day_13.txt")

with open(input_path, "r") as f:
    puzzle_input = f.readlines()
    puzzle_input = [item.strip() for item in puzzle_input]

dot_list = []
fold_list = []
dots = True

for line in puzzle_input:
    if line == "":
        dots = False
    elif dots:
        dot_list.append([int(num) for num in line.split(",")])
    else:
        axis = line.split()[-1].split("=")[0]
        coord = int(line.split()[-1].split("=")[1])
        fold_list.append([axis, coord])

x_max = 0
y_max = 0

for dot in dot_list:
    x_max = max(dot[0], x_max)
    y_max = max(dot[1], y_max)

array = np.zeros([y_max + 1, x_max + 1])

for dot in dot_list:
    array[dot[1], dot[0]] = 1

# Part 1.
fold = fold_list[0]

if fold[0] == "y":
    arr_1 = array[: fold[1], :]
    arr_2 = np.flip(array[fold[1] + 1 :, :], axis=0)
    array = np.clip(arr_1 + arr_2, 0, 1)
else:
    arr_1 = array[:, : fold[1]]
    arr_2 = np.flip(array[:, fold[1] + 1 :], axis=1)
    array = np.clip(arr_1 + arr_2, 0, 1)

print(f"Part 1: {int(array.sum())}")

# Part 2.
for fold in fold_list[1:]:
    if fold[0] == "y":
        arr_1 = array[: fold[1], :]
        arr_2 = np.flip(array[fold[1] + 1 :, :], axis=0)
        array = np.clip(arr_1 + arr_2, 0, 1)
    else:
        arr_1 = array[:, : fold[1]]
        arr_2 = np.flip(array[:, fold[1] + 1 :], axis=1)
        array = np.clip(arr_1 + arr_2, 0, 1)
