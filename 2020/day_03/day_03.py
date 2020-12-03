import os
import pandas as pd

curr_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(
    os.path.join(curr_dir, "data.txt"),
    sep=' ',
    header=None,
    names=['raw']
)

df['raw'] = df['raw'].str.replace('', ' ')
geo = df['raw'].str.split(' ', expand=True).drop([0, 32], axis=1)

def count_trees(geo_in, x_inc, y_inc):
    len_x = geo_in.shape[1]
    len_y = geo_in.shape[0]
    c = 0
    x = 0
    y = 0

    while True:
        if geo_in.iloc[y, x] == '#':
            c += 1

        x += x_inc
        y += y_inc

        x = x % len_x

        if y > len_y -1:
            break

    return c

# Part 1.
c_part_1 = count_trees(geo, 3, 1)
print(c_part_1)

# Part 2.
m = 1

for incs in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
    c_inc = count_trees(geo, incs[0], incs[1])
    m = m * c_inc

print(m)
