import datetime
import os
import re

from ScPy.common import print_color

t_start = datetime.datetime.now()
curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "data.txt"))
txt = f.readlines()
f.close()

txt_cleaned = [item.strip() for item in txt]
# print(txt_cleaned)

# Part 1.
req_list = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
fields_missing = len(req_list)
valid_count = 0

for idx, item in enumerate(txt_cleaned):
    if len(item) > 0:
        for req in req_list:
            if req in item:
                fields_missing -= 1
    else:
        if fields_missing == 0:
            valid_count += 1

        fields_missing = len(req_list)

# Check final item.
if fields_missing == 0:
    valid_count += 1

print(f"Valid part 1: {valid_count}")

# Part 2.
def check_line(line, fields_missing, fields_valid, valid_count):
    if len(item) > 0:
        for field in item.split():
            key = field.split(':')[0]
            value = field.split(':')[1]

            if key == 'byr':
                fields_missing -= 1
                if (
                    value.isdigit()
                    and len(value) == 4
                    and 1920 <= int(value) <= 2002
                ):
                    fields_valid += 1

            elif key == 'iyr':
                fields_missing -= 1
                if (
                    value.isdigit()
                    and len(value) == 4
                    and 2010 <= int(value) <= 2020
                ):
                    fields_valid += 1

            elif key == 'eyr':
                fields_missing -= 1
                if (
                    value.isdigit()
                    and len(value) == 4
                    and 2020 <= int(value) <= 2030
                ):
                    fields_valid += 1

            elif key == 'hgt':
                fields_missing -= 1
                number = value[:-2]
                unit = value[-2:]

                if unit == 'cm':
                    if (
                        number.isdigit()
                        and 150 <= int(number) <= 193
                    ):
                        fields_valid += 1

                elif unit == 'in':
                    if (
                        number.isdigit()
                        and 59 <= int(number) <= 76
                    ):
                        fields_valid += 1

            elif key == 'hcl':
                fields_missing -= 1
                regexp = re.compile(r'#[a-f0-9]{6}')
                if regexp.search(value):
                    fields_valid += 1

            elif key == 'ecl':
                fields_missing -= 1
                if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    fields_valid += 1

            elif key == 'pid':
                fields_missing -= 1
                regexp = re.compile(r'[0-9]{9}')
                if (
                    regexp.search(value)
                    and len(value) == 9
                ):
                    fields_valid += 1

    else:
        if (
            fields_missing == 0
            and fields_valid == len(req_list)
        ):
            valid_count += 1

        fields_missing = len(req_list)
        fields_valid = 0

    return fields_missing, fields_valid, valid_count

req_list = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
fields_missing = len(req_list)
fields_valid = 0
valid_count = 0

for item in txt_cleaned:
    fields_missing, fields_valid, valid_count = check_line(item, fields_missing, fields_valid, valid_count)

# Check last entry.
if (
    fields_missing == 0
    and fields_valid == len(req_list)
):
    valid_count += 1

print(f"\nValid part 2: {valid_count}")
t_end = datetime.datetime.now()
print(f"Time: {t_end-t_start}")
