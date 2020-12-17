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

def iterate(d, k, n):
    for i in range(n):
        c = convolve(d, k, mode='constant')
        inactivate = ((d == 1) & (c < 2)) | ((d == 1) & (c > 3))
        activate = ((d == 0) & (c == 3))
        d[inactivate] = 0
        d[activate] = 1

    return np.sum(np.sum(np.sum(d)))

a = df.values
a = a.reshape(a.shape + (1,))
d = np.zeros([a.shape[0]+12, a.shape[1]+12, 13])
d[6:-6, 6:-6, 6:-6] = a
k = np.ones([3,3,3])
k[1,1,1] = 0

for n in range(6):
    c = convolve(d, k, mode='constant')
    inactivate = ((d == 1) & (c < 2)) | ((d == 1) & (c > 3))
    activate = ((d == 0) & (c == 3))
    d[inactivate] = 0
    d[activate] = 1

print(f"Number active: {np.sum(np.sum(np.sum(d)))}")