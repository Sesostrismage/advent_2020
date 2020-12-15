import datetime
import numpy as np

def memory_game(a, l, s, stop):
    for i in np.arange(start=s, stop=stop):
        if a[int(l), 0] == 0:
            a[int(l), 0] = i - 1
            l = 0
        else:
            l_new = i - 1 - a[int(l), 0]
            a[int(l), 0] = i - 1
            l = l_new

    return l

# Test.
array = np.zeros([11, 1])
array[0] = 1
array[3] = 2

# print(array)

last = 6
last = memory_game(array, last, 4, 11)
print(f"Test 1 result: {last}")

# Test.
array = np.zeros([2021, 1])
array[0] = 1
array[3] = 2
last = 6
last = memory_game(array, last, 4, 2021)
print(f"Test 2 results: {last}")

# Part 1.
array = np.zeros([2021, 1])
array[2] = 1
array[15] = 2
array[0] = 3
array[9] = 4
array[1] = 5
last = 20
last = memory_game(array, last, 7, 2021)
print(f"Part 1 results: {last}")

t_start = datetime.datetime.now()
# Part 2.
array = np.zeros([30000001, 1])
array[2] = 1
array[15] = 2
array[0] = 3
array[9] = 4
array[1] = 5
last = 20
last = memory_game(array, last, 7, 30000001)
print(f"Part 2 results: {last}")

t_end = datetime.datetime.now()

print(f"Part 2 time: {t_end - t_start}")