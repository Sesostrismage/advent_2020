from collections import Counter
from pathlib import Path

import pandas as pd

curr_dir = Path(__file__).parent
input_path = curr_dir / "puzzle_input_day_01.txt"
puzzle_input = pd.read_csv(input_path, header=None, sep="   ")

l1 = puzzle_input.copy(deep=True).iloc[:, 0].sort_values(ignore_index=True)
l2 = puzzle_input.copy(deep=True).iloc[:, 1].sort_values(ignore_index=True)

dist = (l1 - l2).abs().sum()

print(f"Part 1: {dist}")

# Part 2.

c1 = Counter(l1)
c2 = Counter(l2)

sim_count = 0

for val, count in c1.items():
    sim_count += val * count * c2[val]

print(f"Part 2: {sim_count}")
