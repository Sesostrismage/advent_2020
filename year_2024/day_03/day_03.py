from pathlib import Path
import re


def mul(seq):
    crop_str_list = seq[4:-1].split(",")
    result = int(crop_str_list[0]) * int(crop_str_list[1])
    return result


curr_dir = Path(__file__).parent
input_path = curr_dir / "puzzle_input_day_03.txt"

with open(input_path, "r") as f:
    text = f.read()

res = 0
pattern = "mul\(\d{1,3},\d{1,3}\)"
matches = re.findall(pattern, text)

for match in matches:
    res += mul(match)

print(f"Part 1: {res}")


pattern = "mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
matches = re.findall(pattern, text)

print(matches)
enabled = True
res = 0

for match in matches:
    if match == "do()":
        enabled = True
    elif match == "don't()":
        enabled = False
    elif enabled:
        res += mul(match)

print(f"Part 2: {res}")
