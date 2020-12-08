import os

from advent_of_code.year_2019.common.intcode import IntCode

curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "data.txt"))
txt = f.readline()
f.close()

code_list = [int(item) for item in txt.split(',')]

ic = IntCode(code_list, 12, 2)
output = ic.run_code()


print(f"Value at position 0: {output}")
