import itertools
import os
import re

curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "data.txt"))
# f = open(os.path.join(curr_dir, "test_part_2.txt"))
txt = f.readlines()
f.close()

txt_cleaned = [item.strip() for item in txt]

mask = "X" * 36
mem = {}

for item in txt_cleaned:
    if item.startswith("mask"):
        mask = item[7:]
    else:
        split = item.split("=")
        address = int(split[0][4:-2])
        address_bin = bin(address)[2:].zfill(36)
        val = int(split[1])

        for idx, m in enumerate(mask):
            if m == "0":
                pass
            elif m == "1":
                address_bin = address_bin[:idx] + m + address_bin[idx + 1 :]

        test = [m.start() for m in re.finditer("X", mask)]
        perm_list = list(itertools.product([0, 1], repeat=len(test)))

        for perm in perm_list:
            for idx, bit in enumerate(test):
                address_bin = (
                    address_bin[:bit] + str(perm[idx]) + address_bin[bit + 1 :]
                )

            mem[address_bin] = val

total = 0

for address in mem:
    total += mem[address]

print(total)
