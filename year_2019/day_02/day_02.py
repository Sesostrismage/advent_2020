import os

from advent_of_code.year_2019.common.intcode import IntCode

curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "data.txt"))
txt = f.readline()
f.close()

code_list = [int(item) for item in txt.split(',')]
code_list[1] = 12
code_list[2] = 2

ic = IntCode(code_list)
ic.run_code()

print(ic.code_out[:5])
print(f"Value at position 0: {ic.code_out[0]}")
