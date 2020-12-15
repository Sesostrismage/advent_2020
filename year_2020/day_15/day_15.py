import numpy as np

# Test.
a = np.array([
    [0, 1],
    [3, 2]
])
last = 6

for i in np.arange(start=4, stop=11):
    find = np.where(a == last)[0]

    if len(find) == 0:
        a = np.concatenate((a, np.array([[last, i-1]])))
        last = 0
    else:
        last = i - a[find[0], 1] - 1
        a[find[0], 1] = i-1

print(a)
print(last)


# Part 2.
# a = np.array([[2, 1]])

# print(a.shape)

# a = np.concatenate(a, np.array([[2, 1]]))
# print(a)

# a[1, 0] = 2
# a[2, 0] = 15
# a[3, 0] = 0
# a[4, 0] = 9
# a[5, 0] = 1
# a[6, 0] = 20

# for i in np.arange(start=6, stop=30000000):
#     last = a[i-1, 0]
#     find = np.where(a == last)[0]

#     if len(find) == 1:
#         print(i)
#         a[i, 0] = 0
#     else:
#         a[i, 0] = i - 1 - find[-2]

# print(a[-1, 0])
