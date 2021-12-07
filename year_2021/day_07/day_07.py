import os
import timeit

import numpy as np

start = timeit.timeit()


curr_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(curr_dir, "puzzle_input_day_07.txt")

with open(input_path, "r") as f:
    puzzle_input = f.readlines()

puzzle_input = np.array([int(num) for num in puzzle_input[0].split(",")])

# Part 1.
def cost_func_flat(crabs: np.array, pos: int) -> int:
    cost = np.abs(crabs - pos).sum()
    return int(cost)


def median_pos(crabs: np.array) -> int:
    return int(np.median(crabs))


min_pos = median_pos(puzzle_input)

print(f"Part 1: Position = {min_pos}, fuel = {cost_func_flat(puzzle_input, min_pos)}")


# Part 2.
def mean_pos(crabs: np.array) -> int:
    return int(round(np.mean(crabs)))


def cost_func_increasing(crabs: np.array, pos: int) -> int:
    dist = np.abs(crabs - pos)
    cost = (dist * (dist + 1)) / 2
    return int(cost.sum())


def sweep_cost(crabs: np.array, guess: int):
    init_cost = cost_func_increasing(crabs, guess)

    if cost_func_increasing(crabs, guess - 1) < init_cost:
        sign = -1
    else:
        sign = 1

    best_pos = guess
    best_cost = init_cost
    n = 1

    while True:
        new_pos = guess + sign * n
        new_cost = cost_func_increasing(crabs, new_pos)
        if new_cost < best_cost:
            best_pos = new_pos
            best_cost = new_cost
        else:
            break

    return best_pos, best_cost


mean_pos = mean_pos(puzzle_input)
pos, cost = sweep_cost(puzzle_input, mean_pos)
print(f"Part 1: Position = {pos}, fuel = {cost}")

print(f"Time: {timeit.timeit() - start}")
