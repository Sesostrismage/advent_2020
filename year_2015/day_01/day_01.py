import logging
import os
import pandas as pd

curr_dir = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(format="%(message)s", level=logging.DEBUG)

# Part 1.
f = open(os.path.join(curr_dir, "input_day_1.txt"), "r")
input_day_1 = f.read()
f.close()

count_up = input_day_1.count("(")
count_down = input_day_1.count(")")

logging.info(f"Part 1: Floor: {count_up - count_down}")

# Part 2.
input_num = pd.Series(list(input_day_1)).map({"(": 1, ")": -1})
cumsum = input_num.cumsum()
first_basement = cumsum.loc[cumsum == -1].index[0]
logging.info(f"Part 2: First basement: {first_basement+1}")
