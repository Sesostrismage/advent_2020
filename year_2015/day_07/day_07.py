import copy
import logging
import os
import pandas as pd

curr_dir = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(format="%(message)s", level=logging.DEBUG)

# Part 1.
f = open(os.path.join(curr_dir, "input_day_07.txt"), "r")
instructions = f.read().split("\n")
f.close()

series = pd.Series()
leftover_instructions = []
count = 0

while True:
    print(f"Iteration {count}, {len(instructions)} instructions remaining.")
    for line in instructions:
        split_line = line.split("->")
        operation = split_line[0].strip()
        receiver = split_line[1].strip()

        if len(operation.split()) == 1:
            opstrip = operation.strip()

            if opstrip.isnumeric():
                series.loc[receiver] = int(opstrip)
            elif opstrip in series.index:
                series.loc[receiver] = series.loc[opstrip]
            else:
                leftover_instructions.append(line)

        elif "NOT" in operation:
            a = operation.split()[-1]

            if a in series.index:
                inp = series[a]
                series.loc[receiver] = 65535 - inp
            else:
                leftover_instructions.append(line)
        else:
            a = operation.split()[0]
            b = operation.split()[-1]

            if "AND" in operation:
                if a.isnumeric() and b in series.index:
                    series.loc[receiver] = int(a) & series[b]
                elif a in series.index and b in series.index:
                    series.loc[receiver] = series[a] & series[b]
                else:
                    leftover_instructions.append(line)
            elif "OR" in operation:
                if a in series.index and b in series.index:
                    series.loc[receiver] = series[a] | series[b]
                else:
                    leftover_instructions.append(line)
            elif "LSHIFT" in operation:
                if a in series.index:
                    series.loc[receiver] = series[a] << int(b)
                else:
                    leftover_instructions.append(line)
            elif "RSHIFT" in operation:
                if a in series.index:
                    series.loc[receiver] = series[a] >> int(b)
                else:
                    leftover_instructions.append(line)

    if len(leftover_instructions) == 0:
        break
    else:
        instructions = copy.deepcopy(leftover_instructions)
        leftover_instructions = []
        series.sort_index(inplace=True)


print(series.loc["a"])
