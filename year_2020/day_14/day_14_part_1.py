import os

curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "data.txt"))
# f = open(os.path.join(curr_dir, "test.txt"))
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
        val = int(split[1])
        val_bin = bin(val)[2:].zfill(36)

        for idx, m in enumerate(mask):
            if m != "X":
                val_bin = val_bin[:idx] + m + val_bin[idx + 1 :]

        mem[address] = val_bin

total = 0

for address in mem:
    total += int(mem[address], 2)

print(total)
