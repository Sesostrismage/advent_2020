import os
import datetime

curr_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(curr_dir, "test_input_day_14.txt")

with open(input_path, "r") as f:
    puzzle_input = f.readlines()

class Polymer:
    def __init__(self, pi: list) -> None:
        pi = [item.strip() for item in pi]
        self.base = pi.pop(0)
        pi.pop(0)
        self.rule_dict = {item.split('->')[0].strip(): item.split('->')[1].strip() for item in pi}

    def insert(self, n: int):
        insert_dict = {}

        for _ in range(n):
            print(_)
            for i in range(1, len(self.base)):
                seq = self.base[i-1:i+1]
                if seq in self.rule_dict:
                    insert_dict[i] = self.rule_dict[seq]

            for i in reversed(sorted(insert_dict.keys())):
                self.base = self.base[:i] + insert_dict[i] + self.base[i:]

    def count(self):
        char_set = set(self.base)
        min_count = 1e9
        max_count = 0

        for char in char_set:
            count = self.base.count(char)
            min_count = min(min_count, count)
            max_count = max(max_count, count)

        return max_count - min_count


# Part 1.
start = datetime.datetime.now()
pol = Polymer(puzzle_input)
pol.insert(10)
print(f"Part 1: {pol.count()} in {(datetime.datetime.now() - start).total_seconds()} seconds.")


# Part 2.
start = datetime.datetime.now()
pol = Polymer(puzzle_input)
pol.insert(40)
print(f"Part 2: {pol.count()} in {(datetime.datetime.now() - start).total_seconds()} seconds.")