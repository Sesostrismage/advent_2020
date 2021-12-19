import copy
import os
import datetime

curr_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(curr_dir, "puzzle_input_day_14.txt")

with open(input_path, "r") as f:
    puzzle_input = f.readlines()
    puzzle_input = [item.strip() for item in puzzle_input]


class Polymer:
    def __init__(self, pi: list) -> None:
        pi_copy = copy.deepcopy(pi)
        base_str = pi_copy.pop(0)
        self.start_letter = base_str[0]
        self.base_dict = {}

        for n in range(len(base_str) - 1):
            base_pair = base_str[n : n + 2]
            if base_pair not in self.base_dict:
                self.base_dict[base_pair] = 1
            else:
                self.base_dict[base_pair] += 1

        pi_copy.pop(0)
        self.rule_dict = {
            item.split("->")[0].strip(): item.split("->")[1].strip() for item in pi_copy
        }

    def insert(self, n: int):
        for _ in range(n):
            pair_list = list(self.base_dict.keys())
            new_pair_dict = {}

            for base_pair in pair_list:
                if self.base_dict[base_pair] == 0:
                    continue

                base_pair_count = self.base_dict[base_pair]

                if base_pair not in new_pair_dict:
                    new_pair_dict[base_pair] = -base_pair_count
                else:
                    new_pair_dict[base_pair] += -base_pair_count

                new_pair_list = [
                    base_pair[0] + self.rule_dict[base_pair],
                    self.rule_dict[base_pair] + base_pair[1],
                ]

                for new_pair in new_pair_list:
                    if new_pair in new_pair_dict:
                        new_pair_dict[new_pair] += base_pair_count
                    else:
                        new_pair_dict[new_pair] = base_pair_count

            for new_pair in new_pair_dict.keys():
                if new_pair in self.base_dict:
                    self.base_dict[new_pair] += new_pair_dict[new_pair]
                else:
                    self.base_dict[new_pair] = new_pair_dict[new_pair]

    def count(self):
        count_dict = {}

        for base_pair in self.base_dict:
            letter = base_pair[1]

            if letter in count_dict:
                count_dict[letter] += self.base_dict[base_pair]
            else:
                count_dict[letter] = self.base_dict[base_pair]

        count_dict[self.start_letter] += 1

        min_num = 1e21
        max_num = 0

        for count in count_dict.values():
            min_num = min(min_num, count)
            max_num = max(max_num, count)

        return max_num - min_num


# Part 1.
start = datetime.datetime.now()
pol = Polymer(puzzle_input)
pol.insert(10)
print(
    f"Part 1: {pol.count()} in {(datetime.datetime.now() - start).total_seconds()} seconds."
)


# Part 2.
start = datetime.datetime.now()
pol = Polymer(puzzle_input)
pol.insert(40)
print(
    f"Part 2: {pol.count()} in {(datetime.datetime.now() - start).total_seconds()} seconds."
)

