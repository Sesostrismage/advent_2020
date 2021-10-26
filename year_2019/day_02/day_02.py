import os

from advent_of_code.year_2019.common.intcode import IntCode

curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "data.txt"))
txt = f.readline()
f.close()

code_list = [int(item) for item in txt.split(",")]

# Part 1.
ic = IntCode(code_list, 12, 2)
output = ic.run_code()

print(f"Value at position 0: {output}")

# Part 2.
desired_output = 19690720

for n in range(100):
    for m in range(100):
        ic = IntCode(code_list, n, m)
        output = ic.run_code()

        if output == desired_output:
            print("Match!")
            print(f"Input 1: {n}, input 2: {m}")
            break

    if output == desired_output:
        break

print(f"Result: {100 * n + m}")
