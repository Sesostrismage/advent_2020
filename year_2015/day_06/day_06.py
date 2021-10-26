import logging
import os
import pandas as pd

curr_dir = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(format="%(message)s", level=logging.DEBUG)

# Part 1.
f = open(os.path.join(curr_dir, "input_day_06.txt"), "r")
input_day_06 = f.read().split("\n")
f.close()

df = pd.DataFrame(-1, columns=range(1000), index=range(1000))

for line in input_day_06:
    if line.startswith("toggle"):
        command = "toggle"
        start = line.split()[1]
        x_start = int(start.split(",")[0])
        y_start = int(start.split(",")[1])
        end = line.split()[-1]
        x_end = int(end.split(",")[0])
        y_end = int(end.split(",")[1])
        df.loc[x_start:x_end, y_start:y_end] *= -1
    else:
        start = line.split()[2]
        x_start = int(start.split(",")[0])
        y_start = int(start.split(",")[1])
        end = line.split()[-1]
        x_end = int(end.split(",")[0])
        y_end = int(end.split(",")[1])

        if line.startswith("turn on"):
            val = 1
        elif line.startswith("turn off"):
            val = -1

        df.loc[x_start:x_end, y_start:y_end] = val

print(f"Part 1 - Lit lights: {int(df[df == 1].sum().sum())}")


# Part 2.
df = pd.DataFrame(0, columns=range(1000), index=range(1000))

for line in input_day_06:
    if line.startswith("toggle"):
        command = "toggle"
        start = line.split()[1]
        x_start = int(start.split(",")[0])
        y_start = int(start.split(",")[1])
        end = line.split()[-1]
        x_end = int(end.split(",")[0])
        y_end = int(end.split(",")[1])
        df.loc[x_start:x_end, y_start:y_end] += 2
    else:
        start = line.split()[2]
        x_start = int(start.split(",")[0])
        y_start = int(start.split(",")[1])
        end = line.split()[-1]
        x_end = int(end.split(",")[0])
        y_end = int(end.split(",")[1])

        if line.startswith("turn on"):
            val = 1
        elif line.startswith("turn off"):
            val = -1

        df.loc[x_start:x_end, y_start:y_end] += val

        if line.startswith("turn off"):
            df.clip(lower=0, inplace=True)

print(f"Part 2 - Total brightness: {int(df.sum().sum())}")
