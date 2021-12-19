import os

"""
This doesn't work yet.
"""

curr_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(curr_dir, "test_input_day_18.txt")

with open(input_path, "r") as f:
    puzzle_input = f.readlines()
    puzzle_input = [item.strip() for item in puzzle_input]

class SnailFishNumber:
    def __init__(self, string: str, depth: int) -> None:
        self.depth = depth
        self.elem_list = []

        open_brackets = 0

        for idx, char in enumerate(string):
            if char == '[':
                open_brackets += 1
            elif char == ']':
                open_brackets -= 1
            elif (char == ',') and (open_brackets == 1):
                split_idx = idx
                break

        elem_str_list = [string[1:split_idx], string[split_idx+1:-1]]

        for elem_str in elem_str_list:
            if elem_str.isdigit():
                elem = int(elem_str)
            else:
                elem = SnailFishNumber(elem_str, self.depth+1)

            self.elem_list.append(elem)

    def reduce_number(self):
        if (self.depth == 4) and isinstance(self.elem_list[0], SnailFishNumber):
            action = 'explode'
            add_left = self.elem_list[0].elem_list[0]
            add_right = self.elem_list[0].elem_list[1]
            self.elem_list[0] = 0
            return action, add_left, add_right
        elif (self.depth == 4) and isinstance(self.elem_list[1], SnailFishNumber):
            action = 'explode'
            add_left = self.elem_list[1].elem_list[0]
            add_right = self.elem_list[1].elem_list[1]
            self.elem_list[1] = 0
            return action, add_left, add_right


for line in puzzle_input:
    sfn = SnailFishNumber(line, 1)
    print(sfn.elem_list)