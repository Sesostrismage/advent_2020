import logging
import os
import pandas as pd

curr_dir = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(format="%(message)s", level=logging.DEBUG)

# Part 1.
f = open(os.path.join(curr_dir, "input_day_3.txt"), "r")
input_day_3 = f.read()
f.close()

coords = pd.DataFrame([[0, 0]], columns=["x", "y"])

for direction in list(input_day_3):
    new_coords = coords.copy().iloc[-1:, :]

    if direction == "^":
        new_coords.iloc[0, 1] += 1
    elif direction == "v":
        new_coords.iloc[0, 1] -= 1
    elif direction == ">":
        new_coords.iloc[0, 0] += 1
    elif direction == "<":
        new_coords.iloc[0, 0] -= 1

    coords = pd.concat([coords, new_coords])

coords.drop_duplicates(inplace=True)
logging.info(f"Part 1: Number houses visited: {len(coords)}")


# Part 2.
santa_coords = pd.DataFrame([[0, 0]], columns=["x", "y"])
robo_coords = pd.DataFrame([[0, 0]], columns=["x", "y"])
turn = "s"

for direction in list(input_day_3):
    if turn == "s":
        new_coords = santa_coords.copy().iloc[-1:, :]
    else:
        new_coords = robo_coords.copy().iloc[-1:, :]

    if direction == "^":
        new_coords.iloc[0, 1] += 1
    elif direction == "v":
        new_coords.iloc[0, 1] -= 1
    elif direction == ">":
        new_coords.iloc[0, 0] += 1
    elif direction == "<":
        new_coords.iloc[0, 0] -= 1

    if turn == "s":
        santa_coords = pd.concat([santa_coords, new_coords])
    else:
        robo_coords = pd.concat([robo_coords, new_coords])

    if turn == "s":
        turn = "r"
    else:
        turn = "s"

total_coords = pd.concat([santa_coords, robo_coords])
total_coords.drop_duplicates(inplace=True)
logging.info(f"Part 2: Number houses visited: {len(total_coords)}")
