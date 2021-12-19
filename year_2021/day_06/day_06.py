import os
import timeit

import numpy as np

start = timeit.timeit()


curr_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(curr_dir, "puzzle_input_day_06.txt")

with open(input_path, "r") as f:
    puzzle_input = f.readlines()

puzzle_input = [int(num) for num in puzzle_input[0].split(",")]


class LanternFish:
    def __init__(self, fish_list: list) -> None:
        self.age_dict = {num: 0 for num in range(8 + 1)}

        for fish in fish_list:
            self.age_dict[fish] += 1

    def count_fish(self) -> int:
        fish_count = 0

        for count in self.age_dict.values():
            fish_count += count

        return fish_count

    def pass_time(self, days: int) -> None:
        for _ in range(days):
            new_fish = self.age_dict[0]

            for age in range(1, 8 + 1):
                self.age_dict[age - 1] = self.age_dict[age]

            self.age_dict[6] += new_fish
            self.age_dict[8] = new_fish


# Part 1.
lantern_fish = LanternFish(puzzle_input)
lantern_fish.pass_time(80)
print(f"Part 1: {lantern_fish.count_fish()}")


# Part 2.
lantern_fish = LanternFish(puzzle_input)
lantern_fish.pass_time(256)
print(f"Part 2: {lantern_fish.count_fish()}")
