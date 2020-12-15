import numpy as np

def memory_game(l, a, s, stop):
    for i in np.arange(start=s, stop=stop):
        find = np.where(a[:, 0] == l)[0]

        if len(find) == 0:
            a = np.concatenate((a, np.array([[l, i-1]])))
            l = 0
        else:
            l = i - 1 - a[find[0], 1]
            a[find[0], 1] = i-1

    return l

# Test.
array = np.array([
    [0, 1],
    [3, 2]
])
last = 6
last = memory_game(last, array, 4, 11)
print(f"Test 1 result: {last}")

# Test.
array = np.array([
    [0, 1],
    [3, 2]
])
last = 6
last = memory_game(last, array, 4, 2021)
print(f"Test 2 results: {last}")

# Part 1.
array = np.array([
    [2, 1],
    [15, 2],
    [0, 3],
    [9, 4],
    [1, 5]
])
last = 20
last = memory_game(last, array, 7, 2021)
print(f"Part 1 results: {last}")

# Part 1.
array = np.array([
    [2, 1],
    [15, 2],
    [0, 3],
    [9, 4],
    [1, 5]
])
last = 20
last = memory_game(last, array, 7, 30000001)
print(f"Part 2 results: {last}")
