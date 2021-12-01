import os

import pandas as pd

curr_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(curr_dir, "input_day_01.txt")
puzzle_input = pd.read_csv(input_path, header=None)

# Part 1.
number_increase = (puzzle_input.diff() > 0).sum()
print(f"Part 1 answer: {number_increase}")

# Part 2.
number_increase = (puzzle_input.diff().rolling(3).sum() > 0).sum()
print(f"Part 2 answer: {number_increase}")
