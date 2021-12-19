import os
import timeit

import numpy as np

start = timeit.timeit()


class BoardStack:
    def __init__(self, inp: list) -> None:
        stack_list = []
        row_list = []

        for line in inp:
            if len(line) == 0:
                if len(row_list) > 0:
                    stack_list += [row_list]
                    row_list = []
            else:
                row_list.append([int(item) for item in line.split()])

        stack_list += [row_list]
        self.stack = np.array(stack_list)
        self.marked = np.ones(self.stack.shape)

    def mark_num(self, num: int):
        self.marked[self.stack == num] = 0

    def bingo(self):
        if (self.marked.sum(axis=1) == 0).any() or (self.marked.sum(axis=2) == 0).any():
            return True
        else:
            return False

    def find_bingo_boards(self):
        x_prod = board_stack.marked.sum(axis=1).prod(axis=1)
        y_prod = board_stack.marked.sum(axis=2).prod(axis=1)
        bingo_board_idx = np.where((x_prod * y_prod) == 0)
        return bingo_board_idx

    def pop_bingo_boards(self):
        bingo_board_idx = self.find_bingo_boards()
        self.stack = np.delete(self.stack, bingo_board_idx, axis=0)
        self.marked = np.delete(self.marked, bingo_board_idx, axis=0)

    def board_sum(self, idx):
        return (self.stack[idx] * self.marked[idx]).sum()

    def number_boards(self):
        return self.stack.shape[0]


curr_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(curr_dir, "puzzle_input_day_04.txt")

with open(input_path, "r") as f:
    puzzle_input = f.readlines()

puzzle_input = [item.strip() for item in puzzle_input]
number_list = [int(item) for item in puzzle_input.pop(0).split(",")]


# Part 1.
board_stack = BoardStack(puzzle_input)

for num in number_list:
    board_stack.mark_num(num)

    if board_stack.bingo():
        bingo_idx = board_stack.find_bingo_boards()
        print(f"Part 1: {int(board_stack.board_sum(bingo_idx[0]) * num)}")
        break

# Part 2.
board_stack = BoardStack(puzzle_input)

for num in number_list:
    board_stack.mark_num(num)

    if (board_stack.bingo()) and (board_stack.number_boards() > 1):
        board_stack.pop_bingo_boards()
    elif (board_stack.bingo()) and (board_stack.number_boards() == 1):
        print(f"Part 2: {int(board_stack.board_sum(0) * num)}")
        break

print(f"Time: {timeit.timeit() - start}")
