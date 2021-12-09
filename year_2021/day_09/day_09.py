import os
import timeit

import numpy as np
import pandas as pd

start = timeit.timeit()


curr_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(curr_dir, "puzzle_input_day_09.txt")

with open(input_path, "r") as f:
    puzzle_input = f.readlines()
    puzzle_input = [line.strip() for line in puzzle_input]

records = []

for line in puzzle_input:
    records += [[int(num) for num in line]]

df = pd.DataFrame.from_records(records)

# Part 1.
diff_bool = (
    (df < df.shift(periods=1, axis=0).fillna(10))
    & (df < df.shift(periods=-1, axis=0).fillna(10))
    & (df < df.shift(periods=1, axis=1).fillna(10))
    & (df < df.shift(periods=-1, axis=1).fillna(10))
)

print(f"Part 1: {((df + 1) * diff_bool).sum().sum()}")


# Part 2.
location_list = [[(x, df.columns[y])] for x, y in zip(*np.where(df.values < 9))]


def check_adjacent(l1, l2):
    adjacent = False

    for c1 in l1:
        for c2 in l2:
            if abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) == 1:
                adjacent = True
                break

        if adjacent:
            break

    return adjacent


basin_list = [location_list.pop(0)]

while True:
    pop_list = []

    for idx, loc in enumerate(location_list):
        if check_adjacent(basin_list[0], loc):
            pop_list.append(idx)

    if len(pop_list) > 0:
        for idx in reversed(pop_list):
            basin_list[0].append(location_list.pop(idx)[0])

    else:
        basin_list.insert(0, location_list.pop(0))

    if len(location_list) == 0:
        break

basin_sizes = pd.Series([len(basin) for basin in basin_list])
basin_sizes_cropped = basin_sizes.sort_values(ascending=False).iloc[:3]

print(f"Part 2: {basin_sizes_cropped.prod()}")
