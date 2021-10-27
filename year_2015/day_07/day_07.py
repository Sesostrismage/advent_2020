import logging
import os
import pandas as pd

curr_dir = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(format="%(message)s", level=logging.DEBUG)

# Part 1.
f = open(os.path.join(curr_dir, "input_day_07.txt"), "r")
input_day_07 = f.read().split("\n")
f.close()

print(input_day_07)

series = pd.Series()

for line in input_day_07:
    split_line = line.split("->")
    operation = split_line[0].strip()
    receiver = split_line[1].strip()

    if operation.isnumeric():
        series.loc[receiver] = int(operation)
    elif "NOT" in operation:
        inp = series[operation.split()[-1]]
        series.loc[receiver] = 65535 - inp
    else:
        a = operation.split()[0]
        b = operation.split()[-1]

        if "AND" in operation:
            series.loc[receiver] = series[a] & series[b]
        elif "OR" in operation:
            series.loc[receiver] = series[a] | series[b]
        elif "LSHIFT" in operation:
            series.loc[receiver] = series[a] << int(b)
        elif "RSHIFT" in operation:
            series.loc[receiver] = series[a] >> int(b)


print(series.sort_index())
