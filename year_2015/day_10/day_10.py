from itertools import groupby

puzzle_input = "1113222113"

# Part 1.
for n in range(40):
    groups = groupby(puzzle_input)
    read_list = [f"{sum(1 for _ in group)}{label}" for label, group in groups]
    puzzle_input = "".join(read_list)

print(f"Part 1: {len(puzzle_input)}")

for n in range(10):
    groups = groupby(puzzle_input)
    read_list = [f"{sum(1 for _ in group)}{label}" for label, group in groups]
    puzzle_input = "".join(read_list)

print(f"Part 2: {len(puzzle_input)}")
