import numpy as np
import os
import pandas as pd

from scipy.ndimage.filters import convolve

curr_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(curr_dir, "data.txt")
# file_path = os.path.join(curr_dir, "test_3.txt")
f = open(file_path)
txt = f.readlines()
f.close()

txt_cleaned = [line.strip() for line in txt]

dir_dict = {'e': [-1, 0], 'ne': [-1, 1], 'nw': [0, 1], 'w': [1, 0], 'sw': [1, -1], 'se': [0, -1]}

def split_directions(dir_str):
    dir_list_str = []
    idx = 0

    while True:
        if idx >= len(dir_str):
            break
        elif dir_str[idx] in ['n', 's']:
            dir_list_str.append(dir_str[idx:idx+2])
            idx += 2
        else:
            dir_list_str.append(dir_str[idx:idx+1])
            idx += 1

    return dir_list_str

def translate_directions(dir_list_str):
    dir_list_coords = [dir_dict[item] for item in dir_list_str]

    return dir_list_coords

def calc_coords(dir_list_coords):
    x = 0
    y = 0

    for item in dir_list_coords:
        x += item[0]
        y += item[1]

    return [x, y]

def place_in_grid(cl):
    df = pd.DataFrame(0, index=range(500, -501, -1), columns=range(-500, 501))

    for c_pair in cl:
        df.loc[c_pair[1], c_pair[0]] = 1

    a = df.values

    return a

def flip_tiles(a, number_flips=100):
    k = np.ones([3, 3])
    k[0, 2] = 0
    k[2, 0] = 0
    k[1, 1] = 0

    for n in range(number_flips):
        c = convolve(a, k, mode='constant')
        white_bool = (a == 1) & ((c == 0) | (c > 2))
        black_bool = (a == 0) & (c == 2)
        a[white_bool] = 0
        a[black_bool] = 1

    return np.sum(np.sum(a))

# Part 1.
coord_list = []

for line in txt_cleaned:
    dls = split_directions(line)
    dlc = translate_directions(dls)
    coords = calc_coords(dlc)

    if coords not in coord_list:
        coord_list.append(coords)
    else:
        coord_idx = coord_list.index(coords)
        coord_list.pop(coord_idx)

print(f"{len(coord_list)} black tiles.")

# Part 2.
array = place_in_grid(coord_list)
number_black_tiles = flip_tiles(array)
print(f"{np.sum(np.sum(array))} black tiles.")
