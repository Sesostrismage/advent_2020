import numpy as np
import os
import pandas as pd

curr_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(
    os.path.join(curr_dir, "data.txt"), sep=" ", header=None, names=["mass"]
)

# Part 1.
df[0] = ((df["mass"] / 3).apply(np.floor) - 2).clip(lower=0)
print(f"Fuel required: {int((df[0]).sum())}")

i = 1

total_fuel = int((df[0]).sum())

while True:
    df[i] = ((df[i - 1] / 3).apply(np.floor) - 2).clip(lower=0)
    extra_fuel = int((df[i]).sum())
    total_fuel += extra_fuel
    i += 1

    if extra_fuel == 0:
        break

print(f"Total fuel required: {total_fuel}")
