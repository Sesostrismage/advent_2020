import numpy as np
import os
import pandas as pd
from scipy.ndimage.filters import convolve


def iterate(a, k, m):
    while True:
        a_prev = np.copy(a)
        c = convolve(a, k, mode="constant")
        vacate_bool = (a == 1) & (c >= 4)
        fill_bool = (a == 0) & (c == 0)
        a[vacate_bool & m] = 0
        a[fill_bool & m] = 1

        print(np.sum(np.sum(a)))

        if np.array_equal(a, a_prev):
            break

    return a


curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "data.txt"))
# f = open(os.path.join(curr_dir, "test.txt"))
txt = f.readlines()
f.close()

txt_cleaned = [item.strip() for item in txt]
txt_split = [list(item) for item in txt_cleaned]
df = pd.DataFrame.from_records(txt_split).replace({"L": 0, ".": np.nan})
print(f"Initial number of seats: {df.notnull().sum().sum()}")

mask = df.notnull().values
array = np.zeros(mask.shape)
kernel = np.ones([3, 3])
kernel[1, 1] = 0

array = iterate(array, kernel, mask)
print(f"{np.sum(np.sum(array))} occupied seats.")
