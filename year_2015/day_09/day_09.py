import itertools
import os
import pandas as pd

curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "input_day_09.txt"), "r")
puzzle_input = f.read().split("\n")
f.close()

distance_df = pd.DataFrame()

for line in puzzle_input:
    origin = line.split()[0].strip()
    destination = line.split()[2].strip()
    distance = int(line.split("=")[-1])
    distance_df.loc[origin, destination] = distance
    distance_df.loc[destination, origin] = distance

distance_df.sort_index(axis=0, inplace=True)
distance_df.sort_index(axis=1, inplace=True)


# Part 1 +2.
shortest_distance = 1e6
longest_distance = 0

for route in itertools.permutations(distance_df.columns):
    distance = 0
    for i in range(1, len(route)):
        distance += distance_df.loc[route[i - 1], route[i]]

    shortest_distance = min(shortest_distance, distance)
    longest_distance = max(longest_distance, distance)

print(f"Part 1 - Shortest distance: {int(shortest_distance)}")
print(f"Part 2 - Longest distance: {int(longest_distance)}")
