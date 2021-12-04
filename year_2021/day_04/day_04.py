import os
import pandas as pd


def create_boards(pi: list) -> list:
    bl = []
    bil = []

    for line in pi:
        if len(line) == 0:
            if len(bil) == 0:
                pass
            else:
                bl.append(pd.DataFrame.from_records(bil))
                bil = []
        else:
            bil.append([int(item) for item in line.split()])

    bl.append(pd.DataFrame.from_records(bil))

    return bl


curr_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(curr_dir, "puzzle_input_day_04.txt")

with open(input_path, "r") as f:
    puzzle_input = f.readlines()

puzzle_input = [item.strip() for item in puzzle_input]

number_list = [int(item) for item in puzzle_input.pop(0).split(",")]


# Part 1.
board_list = create_boards(puzzle_input)
stop_drawing = False

for number in number_list:
    for board in board_list:
        board[board == number] = 0

        if (board.sum(axis=0) == 0).any() or (board.sum(axis=1) == 0).any():
            stop_drawing = True
            break

    if stop_drawing:
        break

print(f"Part 1: {board.sum().sum() * number}")


# Part 2.
board_list = create_boards(puzzle_input)
stop_drawing = False

for number in number_list:
    for board in board_list:
        board[board == number] = 0

    for idx in reversed(range(len(board_list))):
        board = board_list[idx]
        if (board.sum(axis=0) == 0).any() or (board.sum(axis=1) == 0).any():
            board_list.pop(idx)

    if len(board_list) == 0:
        break

print(f"Part 2: {board.sum().sum() * number}")
