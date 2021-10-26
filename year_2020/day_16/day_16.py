import os
import pandas as pd

curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "data.txt"))
# f = open(os.path.join(curr_dir, "test_part_1.txt"))
# f = open(os.path.join(curr_dir, "test_part_2.txt"))
txt = f.readlines()
f.close()

txt_cleaned = [line.strip() for line in txt if line != "\n"]


def extract_numbers(l, vr, r):
    parts = l.split(":")[1].split()
    rule_name = l.split(":")[0]
    r[rule_name] = []

    for part in [parts[0], parts[2]]:
        start = int(part.split("-")[0])
        end = int(part.split("-")[-1])
        vr += list(range(start, end + 1))
        r[rule_name] += list(range(start, end + 1))

    return vr, r


def check_ticket(l, e, vr):
    v = True

    for n in l.split(","):
        if not int(n) in vr:
            e += int(n)
            v = False

    return e, v, vr


# Part 1.
valid_range = []
valid_ticket_list = []
error = 0
rules_dict = {}

state = "rules"

for line in txt_cleaned:
    if state == "rules" and line != "your ticket:":
        valid_range, rules = extract_numbers(line, valid_range, rules_dict)
    elif line == "your ticket:":
        state = "my_ticket"
    elif line == "nearby tickets:":
        state = "nearby_tickets"
    elif state == "my_ticket":
        my_ticket = [int(field) for field in line.split(",")]
    elif state == "nearby_tickets":
        error, valid_ticket, valid_range = check_ticket(line, error, valid_range)

        if valid_ticket:
            valid_ticket_list.append([int(number) for number in line.split(",")])

valid_range = sorted(list(set(valid_range)))
print(f"Ticket scanning error rate: {error}")

# Part 2.
ticket_df = pd.DataFrame.from_records(valid_ticket_list)

possible_fields_dict = {col: [] for col in ticket_df.columns}

for field in possible_fields_dict:
    for rule in rules_dict:
        if ticket_df[field].isin(rules_dict[rule]).all():
            possible_fields_dict[field].append(rule)

guessed_fields_dict = {}

while True:
    if len(possible_fields_dict) == 0:
        break

    for col in possible_fields_dict:
        if len(possible_fields_dict[col]) == 1:
            field = possible_fields_dict[col][0]
            column = col
            break

    possible_fields_dict.pop(column)
    guessed_fields_dict[column] = field

    for column in possible_fields_dict:
        if field in possible_fields_dict[column]:
            possible_fields_dict[column].pop(possible_fields_dict[column].index(field))

multiplier = 1

for idx, number in enumerate(my_ticket):
    if guessed_fields_dict[idx][:9] == "departure":
        multiplier = multiplier * number

print(f"Part 2 answer: {multiplier}")
