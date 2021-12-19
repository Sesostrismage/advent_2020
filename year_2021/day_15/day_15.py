import numpy as np
import os
import datetime

"""
This doesn't work yet.
"""

curr_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(curr_dir, "puzzle_input_day_15.txt")

with open(input_path, "r") as f:
    puzzle_input = f.readlines()
    puzzle_input = [item.strip() for item in puzzle_input]

records = []

for line in puzzle_input:
    records += [[int(num) for num in line]]

array = np.array(records)
array[0][0] = 0

old_path_list = [[(0, 0)]]
max_x = array.shape[0] - 1
max_y = array.shape[1] - 1

steps = array.shape[0] + array.shape[1] - 2

for n in range(steps):
    print(n)
    new_path_list = []
    for path in old_path_list:
        x = path[-1][0]
        y = path[-1][1]

        if x +1 <= max_x:
            new_path_list.append(path + [(x+1,y)])
        if y+1 <= max_y:
            new_path_list.append(path + [(x,y+1)])

    old_path_list = new_path_list

print(f"Path list length: {len(old_path_list)}")

def cost_func(arr: np.array, path_list: list) -> int:
    min_cost = 1e9

    for path in path_list:
        cost = 0
        for step in path:
            cost += array[step[0], step[1]]

        min_cost = min(min_cost, cost)

    return min_cost

print(cost_func(array, old_path_list))
