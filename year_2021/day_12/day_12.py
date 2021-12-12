import os
import timeit

import numpy as np
import pandas as pd

start = timeit.timeit()

curr_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(curr_dir, "puzzle_input_day_12.txt")


class Path:
    def __init__(self, pi: list) -> None:
        self.connections = {}

        for line in pi:
            if (line[0] in self.connections) and (line[1] != "start"):
                self.connections[line[0]].append(line[1])
            elif line[1] != "start":
                self.connections[line[0]] = [line[1]]

            if (line[1] in self.connections) and (line[0] != "start"):
                self.connections[line[1]].append(line[0])
            elif line[0] != "start":
                self.connections[line[1]] = [line[0]]

        self.paths = []

    def explore(self, allow_doublet: bool):
        open_path_list = [["start"]]

        while len(open_path_list) > 0:
            new_path_list = []

            for path in open_path_list:
                for conn in self.connections[path[-1]]:
                    is_small = conn == conn.lower()

                    if (
                        (is_small)
                        and (
                            (conn not in path)
                            or (
                                (allow_doublet)
                                and (not self.small_doublet_in_path(path))
                            )
                        )
                    ) or (not is_small):
                        new_path = path + [conn]
                        if new_path[-1] == "end":
                            self.paths.append(new_path)
                        else:
                            new_path_list.append(new_path)

            open_path_list = new_path_list

    def small_doublet_in_path(self, path) -> bool:
        doublet = False

        for node in path:
            is_small = node == node.lower()
            if (path.count(node) > 1) and is_small:
                doublet = True
                break

        return doublet


with open(input_path, "r") as f:
    puzzle_input = f.readlines()
    puzzle_input = [item.strip().split("-") for item in puzzle_input]

# Part 1.
path = Path(puzzle_input)
path.explore(allow_doublet=False)
print(f"Path 1: {len(path.paths)}")

# Part 2.
path = Path(puzzle_input)
path.explore(allow_doublet=True)
print(f"Part 2: {len(path.paths)}")
