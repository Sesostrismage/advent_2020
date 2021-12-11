import os
import timeit

import numpy as np

start = timeit.timeit()


curr_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(curr_dir, "puzzle_input_day_08.txt")

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

        self.output_list = [set(item) for item in puzzle_line.split("|")[1].split()]
        self.in_out_map = {letter: None for letter in "abcdefg"}
        self.wire_map = {}

    def count_unique(self):
        count = 0

        for item in self.output_list:
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

        if (digit_4 is not None) and (digit_7 is not None):
            for l6 in self.signal_dict[6]:
                diff = l6 - digit_4 - digit_7
                if len(diff) == 1:
                    g_wire = diff.pop()
                    self.in_out_map[g_wire] = "g"

                    for wire in "abcdefg":
                        if self.in_out_map[wire] is None:
                            e_wire = wire
                            self.in_out_map[e_wire] = "e"
                            break

        self.wire_map["0"] = set([a_wire, b_wire, c_wire, e_wire, f_wire, g_wire])
        self.wire_map["1"] = set([c_wire, f_wire])
        self.wire_map["2"] = set([a_wire, c_wire, d_wire, e_wire, g_wire])
        self.wire_map["3"] = set([a_wire, c_wire, d_wire, f_wire, g_wire])
        self.wire_map["4"] = set([b_wire, c_wire, d_wire, f_wire])
        self.wire_map["5"] = set([a_wire, b_wire, d_wire, f_wire, g_wire])
        self.wire_map["6"] = set([a_wire, b_wire, d_wire, e_wire, f_wire, g_wire])
        self.wire_map["7"] = set([a_wire, c_wire, f_wire])
        self.wire_map["8"] = set(["a", "b", "c", "d", "e", "f", "g"])
        self.wire_map["9"] = set([a_wire, b_wire, c_wire, d_wire, f_wire, g_wire])

    def show_output(self):
        num_str = ""
        for output in self.output_list:
            for num, segments in self.wire_map.items():
                if output == segments:
                    num_str += num
                    break

        num = int(num_str)
        return num


unique_count = 0

# Part 1.
for line in puzzle_input:
    ssd = SSD(line)
    unique_count += ssd.count_unique()

print(f"Part 1: {unique_count}")


# Part 2.
signal_sum = 0

for line in puzzle_input:
    ssd = SSD(line)
    ssd.map_wires()
    signal_sum += ssd.show_output()

print(f"Part 2: {signal_sum}")
