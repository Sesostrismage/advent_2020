import os
import timeit

import numpy as np
import pandas as pd

start = timeit.timeit()


class Octopus:
    def __init__(self, pi) -> None:
        records = []

        for line in pi:
            records += [[int(num) for num in line]]

        self.array = np.array(records)
        self.neighbours = [
            [-1, 1],
            [0, 1],
            [1, 1],
            [1, 0],
            [1, -1],
            [0, -1],
            [-1, -1],
            [-1, 0],
        ]

    def increase(self):
        self.array += 1

    def flash(self, steps, check_synchronized=False):
        flash_count = 0

        for n in range(steps):
            self.increase()
            flash_mask = np.full(self.array.shape, True)

            while True:
                flash_count_loop = 0

                for iy, ix in np.ndindex(octopus.array.shape):
                    if (self.array[iy, ix] > 9) and (flash_mask[iy, ix]):
                        flash_count_loop += 1
                        flash_mask[iy, ix] = False

                        for neighbour in self.neighbours:
                            ny = iy + neighbour[0]
                            nx = ix + neighbour[1]

                            if (0 <= ny < self.array.shape[0]) and (
                                0 <= nx < self.array.shape[1]
                            ):
                                self.array[ny, nx] += 1

                flash_count += flash_count_loop

                if flash_count_loop == 0:
                    break

            self.array[self.array > 9] = 0

            if check_synchronized and (flash_mask == False).all():
                return n +1

        return flash_count


curr_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(curr_dir, "puzzle_input_day_11.txt")

with open(input_path, "r") as f:
    puzzle_input = f.readlines()
    puzzle_input = [item.strip() for item in puzzle_input]

# Part 1.
octopus = Octopus(puzzle_input)
flashes = octopus.flash(100)
print(f"Part 1: {flashes}")

# Part 2.
octopus = Octopus(puzzle_input)
flashes = octopus.flash(1000, check_synchronized=True)
print(f"Part 2: {flashes}")