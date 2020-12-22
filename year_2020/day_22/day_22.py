import os

curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "data.txt"))
# f = open(os.path.join(curr_dir, "test.txt"))
# f = open(os.path.join(curr_dir, "test_2.txt"))

p1_list = []
p2_list = []
state = None

for line in f.readlines():
    if line == 'Player 1:\n':
        state = 'p1'
    elif line == 'Player 2:\n':
        state = 'p2'
    elif state == 'p1' and line != '\n':
        p1_list.append(int(line.strip()))
    elif state == 'p2' and line != '\n':
        p2_list.append(int(line.strip()))

f.close()

print(p1_list, p2_list)

def calc_score(card_list):
    m = 1
    s = 0

    for card in reversed(card_list):
        s += card * m
        m += 1

    return s

while True:
    p1_card = p1_list.pop(0)
    p2_card = p2_list.pop(0)

    if p1_card > p2_card:
        p1_list += [p1_card, p2_card]
    else:
        p2_list += [p2_card, p1_card]

    if len(p1_list) == 0:
        score = calc_score(p2_list)
        break
    elif len(p2_list) == 0:
        score = calc_score(p1_list)
        break

print(score)