import numpy as np
import os
import pandas as pd
from scipy.ndimage.filters import convolve

curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "data.txt"))
# f = open(os.path.join(curr_dir, "test_part_1.txt"))
txt = f.readlines()
f.close()

txt_cleaned = [item.strip() for item in txt]
txt_split = [list(item) for item in txt_cleaned]
df = pd.DataFrame.from_records(txt_split).replace({'#': 1, '.': 0})
a = df.values

def iterate(d, k, n):
    for _ in range(n):
        c = convolve(d, k, mode='constant')
        inactivate = ((d == 1) & (c < 2)) | ((d == 1) & (c > 3))
        activate = ((d == 0) & (c == 3))
        d[inactivate] = 0
        d[activate] = 1

    return d


# Part 1.
a_part_1 = a.reshape(a.shape + (1,))
dimension = np.zeros([a_part_1.shape[0]+12, a_part_1.shape[1]+12, 13])
dimension[6:-6, 6:-6, 6:-6] = a_part_1
kernel = np.ones([3,3,3])
kernel[1,1,1] = 0
dimension = iterate(dimension, kernel, 6)
print(f"Number active, part 1: {np.sum(np.sum(np.sum(dimension)))}")

# Part 2.
a_part_1 = a.reshape(a.shape + (1,) + (1,))
dimension = np.zeros([a_part_1.shape[0]+12, a_part_1.shape[1]+12, 13, 13])
dimension[6:-6, 6:-6, 6:-6, 6:-6] = a_part_1
kernel = np.ones([3,3,3,3])
kernel[1,1,1,1] = 0
dimension = iterate(dimension, kernel, 6)
print(f"Number active, part 2: {np.sum(np.sum(np.sum(np.sum(dimension))))}")
