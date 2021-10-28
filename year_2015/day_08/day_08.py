import os
import re

curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "input_day_08.txt"), "r")
puzzle_input = f.read().split("\n")
f.close()

# Part 1.
total_code_length = 0
total_str_length = 0

for line in puzzle_input:
    code_length = len(line)
    stripline = line[1:-1]
    str_length = len(stripline)
    single_escape_pattern = r"""\\\"|\\\\"""
    str_length -= len(re.findall(single_escape_pattern, line))
    hex_char_pattern = r"""\\x[0-91-f]{2}"""
    str_length -= 3 * len(re.findall(hex_char_pattern, line))

    total_code_length += code_length
    total_str_length += str_length

print(f"Part 1: {total_code_length-total_str_length}")


# Part 2.
total_code_length = 0
total_encoded_length = 0

for line in puzzle_input:
    code_length = len(line)
    encoded_length = len(line) + 2
    encoded_length += line.count('"')
    encoded_length += line.count("\\")
    # print(f"Code length: {code_length}")
    # print(f"Encoded length: {encoded_length}")

    total_code_length += code_length
    total_encoded_length += encoded_length


print(f"Part 2: {total_encoded_length-total_code_length}")
