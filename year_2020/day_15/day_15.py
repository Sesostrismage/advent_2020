import datetime
import numpy as np

def memory_game(m, l, s, stop):
    for i in np.arange(start=s, stop=stop):
        if l not in m:
            m[l] = i - 1
            l = 0
        else:
            l_new = i - 1 - m[l]
            m[l] = i - 1
            l = l_new

    return l

# Test.
mem = {}
mem[0] = 1
mem[3] = 2
last = 6
last = memory_game(mem, last, 4, 11)
print(f"Test 1 result: {last}")

# Test.
mem = {}
mem[0] = 1
mem[3] = 2
last = 6
last = memory_game(mem, last, 4, 2021)
print(f"Test 2 results: {last}")

# Part 1.
mem = {}
mem[2] = 1
mem[15] = 2
mem[0] = 3
mem[9] = 4
mem[1] = 5
last = 20
last = memory_game(mem, last, 7, 2021)
print(f"Part 1 results: {last}")

t_start = datetime.datetime.now()
# Part 2.
mem = {}
mem[2] = 1
mem[15] = 2
mem[0] = 3
mem[9] = 4
mem[1] = 5
last = 20
last = memory_game(mem, last, 7, 30000001)
print(f"Part 2 results: {last}")

t_end = datetime.datetime.now()

print(f"Part 2 time: {t_end - t_start}")
