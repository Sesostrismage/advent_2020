import numpy as np
import os
import pandas as pd

curr_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(
    os.path.join(curr_dir, "data.txt"),
    sep=' ',
    header=None,
    names=['mass']
)

# Part 1.
df['fuel'] = (df['mass']/3).apply(np.floor) - 2
print(f"Fuel required: {int((df['fuel']).sum())}")