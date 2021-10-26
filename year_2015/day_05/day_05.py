import logging
import os
import re

curr_dir = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(format="%(message)s", level=logging.DEBUG)

# Part 1.
f = open(os.path.join(curr_dir, "input_day_5.txt"), "r")
input_day_5 = f.read().split("\n")
f.close()

nice_count = 0

for line in input_day_5:
    vowels = len(re.findall(r"[aeiou]", line)) >= 3
    repeats = len(re.findall(r"([a-z])\1{1,}", line)) >= 1
    bad_strings = len(re.findall(r"ab|cd|pq|xy", line)) == 0

    if vowels and repeats and bad_strings:
        nice_count += 1

print(f"Part 1 - Nice strings: {nice_count}")


# Part 2.
nice_count = 0

for line in input_day_5:
    two_letter_pairs = len(re.findall(r"([a-z][a-z]).*?\1", line)) > 0
    letter_spaced = len(re.findall(r"([a-z]).\1", line)) > 0

    if two_letter_pairs and letter_spaced:
        nice_count += 1

print(f"Part 2 - Nice strings: {nice_count}")
