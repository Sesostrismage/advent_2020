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
        self.signal_list = [set(item) for item in puzzle_line.split("|")[0].split()]
        self.signal_dict = {}

        for signal in self.signal_list:
            l = len(signal)

            if l not in self.signal_dict:
                self.signal_dict[l] = [signal]
            else:
                self.signal_dict[l].append(signal)

        self.output_dict = {
            idx: set(item) for idx, item in enumerate(puzzle_line.split("|")[1].split())
        }
        self.in_out_map = {letter: None for letter in "abcdefg"}

    def count_unique(self):
        count = 0

        for item in self.output_dict.values():
            if len(item) in [2, 3, 4, 7]:
                count += 1

        return count

    def get_first(self, length):
        if len(self.signal_dict[length]) > 0:
            return self.signal_dict[length][0]
        else:
            return None

    def get_wire_from_segment(self, val):
        key = None

        for k, v in self.in_out_map.items():
            if v == val:
                key = k
                break

        return key

    def map_wires(self):
        digit_1 = self.get_first(2)
        digit_7 = self.get_first(3)
        digit_4 = self.get_first(4)

        if (digit_1 is not None) and (digit_7 is not None):
            self.in_out_map[(digit_7 - digit_1).pop()] = "a"

        if (digit_7 is not None) and (digit_4 is not None):
            self.in_out_map[(digit_7 - digit_4).pop()] = "a"

        for l6 in self.signal_dict[6]:
            if digit_1 is not None:
                if len(digit_1 - l6) == 1:
                    self.in_out_map[(digit_1 - l6).pop()] = "c"
                    continue

        a_wire = self.get_wire_from_segment("a")
        c_wire = self.get_wire_from_segment("c")

        if (digit_1 is not None) and (c_wire is not None):
            f_wire = (digit_1 - set([c_wire])).pop()
            self.in_out_map[f_wire] = "f"

        if digit_4 is not None:
            for l5 in self.signal_dict[5]:
                diff = digit_4 - l5
                if (len(diff) == 1) and (c_wire is not None) and (diff != set(c_wire)):
                    self.in_out_map[diff.pop()] = "b"

        b_wire = self.get_wire_from_segment("b")

        if (
            (digit_4 is not None)
            and (b_wire is not None)
            and (c_wire is not None)
            and (f_wire is not None)
        ):
            d_wire = (digit_4 - set(b_wire) - set(c_wire) - set(f_wire)).pop()
            self.in_out_map[d_wire] = "d"
        else:
            d_wire = None


unique_count = 0

# Part 1.
for line in puzzle_input:
    ssd = SSD(line)
    unique_count += ssd.count_unique()

print(f"Part 1: {unique_count}")


# Part 2.
for line in puzzle_input:
    ssd = SSD(line)
    ssd.map_wires()
    print(ssd.in_out_map)
