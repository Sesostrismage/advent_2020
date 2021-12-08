import os
import timeit

import numpy as np

start = timeit.timeit()


curr_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(curr_dir, "test_input_day_08.txt")

with open(input_path, "r") as f:
    puzzle_input = f.readlines()


class SSD:
    def __init__(self, puzzle_line: str) -> None:
        self.signal_list = puzzle_line.split("|")[0].split()
        self.output_dict = {
            idx: set(item) for idx, item in enumerate(puzzle_line.split("|")[1].split())
        }
        self.unmapped_outputs = {
            idx: set(item) for idx, item in enumerate(puzzle_line.split("|")[1].split())
        }
        self.number_mapping = {n: None for n in range(10)}
        self.size_dict = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}

    def count_unique(self):
        count = 0

        for item in self.output_dict.values():
            if len(item) in [2, 3, 4, 7]:
                count += 1

        return count

    def map_components(self):
        # Map unambiguous values.
        idx_list = self.output_dict.keys()
        for idx in idx_list:
            if len(self.output_dict[idx]) == 2:
                self.number_mapping[1] = set(self.output_dict[idx])
                self.unmapped_outputs.pop(idx)
            elif len(self.output_dict[idx]) == 3:
                self.number_mapping[7] = set(self.output_dict[idx])
                self.unmapped_outputs.pop(idx)
            elif len(self.output_dict[idx]) == 4:
                self.number_mapping[4] = set(self.output_dict[idx])
                self.unmapped_outputs.pop(idx)

        # Map length 5 values.
        idx_list = self.output_dict.keys()

        for idx in idx_list:
            val = self.output_dict[idx]
            if len(val) == 5:
                if (self.number_mapping[1] is not None) and (
                    self.number_mapping[1] <= val
                ):
                    self.number_mapping[3] = val
                    self.unmapped_outputs.pop(idx)
                elif (self.number_mapping[7] is not None) and (
                    self.number_mapping[7] <= val
                ):
                    self.number_mapping[3] = val
                    self.unmapped_outputs.pop(idx)
                elif (self.number_mapping[4] is not None) and (
                    len(self.number_mapping[4] & val) == 2
                ):
                    self.number_mapping[2] = val
                    self.unmapped_outputs.pop(idx)
                elif (self.number_mapping[4] is not None) and (
                    len(self.number_mapping[4] & val) == 3
                ):
                    self.number_mapping[5] = val
                    self.unmapped_outputs.pop(idx)

        # Map length 6 values.
        idx_list = self.output_dict.keys()

        for idx in idx_list:
            if len(val) == 6:
                if (self.number_mapping[4] is not None) and (
                    self.number_mapping[4] <= val
                ):
                    self.number_mapping[9] = val
                    self.unmapped_outputs.pop(idx)
                elif (self.number_mapping[7] is not None) and (
                    self.number_mapping[7] <= val
                ):
                    self.number_mapping[9] = val
                    self.unmapped_outputs.pop(idx)

    def __remove_from_unmapped(self, letter):
        pass


unique_count = 0

# Part 1.
for line in puzzle_input:
    ssd = SSD(line)
    unique_count += ssd.count_unique()

print(f"Part 1: {unique_count}")


# Part 2.
for line in puzzle_input:
    ssd = SSD(line)
    ssd.map_components()
    print(ssd.unmapped_outputs)
