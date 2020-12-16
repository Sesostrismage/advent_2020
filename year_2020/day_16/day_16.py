import os

curr_dir = os.path.dirname(os.path.abspath(__file__))

# f = open(os.path.join(curr_dir, "data.txt"))
# f = open(os.path.join(curr_dir, "test_part_1.txt"))
f = open(os.path.join(curr_dir, "test_part_2.txt"))
txt = f.readlines()
f.close()

txt_cleaned = [line.strip() for line in txt if line != '\n']

# print(txt_cleaned)

def extract_numbers(l, vr, r):
    parts = l.split(':')[1].split()
    rule_name = l.split(':')[0]
    r[rule_name] = []

    for part in [parts[0], parts[2]]:
        start = int(part.split('-')[0])
        end = int(part.split('-')[-1])
        vr += list(range(start, end+1))
        r[rule_name] += list(range(start, end+1))

    return vr, r

def check_ticket(l, e, vr):
    v = True

    for number in l.split(','):
        if not int(number) in vr:
            e += int(number)
            v = False

    return e, v, vr

# Part 1.
valid_range = []
valid_ticket_list = []
error = 0
rules = {}

state = 'rules'

for line in txt_cleaned:
    if state == 'rules' and line != 'your ticket:':
        valid_range, rules = extract_numbers(line, valid_range, rules)
    elif line == 'your ticket:':
        state = 'my_ticket'
    elif line == 'nearby tickets:':
        state = 'nearby_tickets'
    elif state == 'nearby_tickets':
        error, valid_ticket, valid_range = check_ticket(line, error, valid_range)

        if valid_ticket:
            valid_ticket_list.append([int(number) for number in line.split(',')])

valid_range = sorted(list(set(valid_range)))
print(f"Ticket scanning error rate: {error}")

# Part 2.
print(valid_ticket_list)

# print(rules)