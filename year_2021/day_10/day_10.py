import os
import timeit

import numpy as np
import pandas as pd

start = timeit.timeit()


curr_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(curr_dir, "puzzle_input_day_10.txt")

with open(input_path, "r") as f:
    puzzle_input = f.readlines()
    puzzle_input = [item.strip() for item in puzzle_input]

pair_dict = {"(": ")", "[": "]", "{": "}", "<": ">"}

# Part 1.
score_dict = {")": 3, "]": 57, "}": 1197, ">": 25137}
score = 0

for line in puzzle_input:
    bracket_list = []
    for char in line:
        if char in pair_dict.keys():
            bracket_list.append(char)
        else:
            if pair_dict[bracket_list[-1]] == char:
                bracket_list.pop(-1)
            else:
                score += score_dict[char]
                break

print(f"Part 1: {score}")


# Part 2.
score = 0
score_list = []


def increase_score(score, char):
    score_dict = {")": 1, "]": 2, "}": 3, ">": 4}
    multiplier = 5
    score *= multiplier
    score += score_dict[char]

    return score


illegal = False

for line in puzzle_input:
    bracket_list = []
    for char in line:
        if char in pair_dict.keys():
            bracket_list.append(char)
        else:
            if pair_dict[bracket_list[-1]] == char:
                bracket_list.pop(-1)
            else:
                illegal = True
                break

    if illegal:
        illegal = False
        continue

    for char in reversed(bracket_list):
        match_char = pair_dict[char]
        score = increase_score(score, match_char)

    score_list.append(score)
    score = 0

print(f"Part 2: {round(np.median(score_list))}")
