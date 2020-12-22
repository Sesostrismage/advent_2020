import os

curr_dir = os.path.dirname(os.path.abspath(__file__))

def load_hands(f_path):
    list_1 = []
    list_2 = []
    state = None

    f = open(f_path)

    for line in f.readlines():
        if line == 'Player 1:\n':
            state = 'p1'
        elif line == 'Player 2:\n':
            state = 'p2'
        elif state == 'p1' and line != '\n':
            list_1.append(int(line.strip()))
        elif state == 'p2' and line != '\n':
            list_2.append(int(line.strip()))

    f.close()

    return list_1, list_2

def calc_score(card_list):
    m = 1
    s = 0

    for card in reversed(card_list):
        s += card * m
        m += 1

    return s

def play_simple_game(list_1, list_2):

    while True:
        p1_card = list_1.pop(0)
        p2_card = list_2.pop(0)

        if p1_card > p2_card:
            list_1 += [p1_card, p2_card]
        else:
            list_2 += [p2_card, p1_card]

        if len(list_1) == 0:
            s = calc_score(list_2)
            break
        elif len(list_2) == 0:
            s = calc_score(list_1)
            break

    return s

def play_recursive_game(list_1, list_2):
    prev_hands_list = []
    game_end = False
    s = 0

    while True:
        if len(prev_hands_list) == 0:
            prev_hands_list.append([list_1.copy(), list_2.copy()])
        else:
            for hands in prev_hands_list:
                if hands[0] == list_1 and hands[1] == list_2:
                    s = calc_score(list_1)
                    print('Game ended by repeated hands.')
                    game_end = True
                    break

            prev_hands_list.append([list_1, list_2])

        if game_end:
            break

        p1_card = list_1.pop(0)
        p2_card = list_2.pop(0)

        if p1_card > p2_card:
            list_1 += [p1_card, p2_card]
        else:
            list_2 += [p2_card, p1_card]

        if len(list_1) == 0:
            s = calc_score(list_2)
            break
        elif len(list_2) == 0:
            s = calc_score(list_1)
            break

    return s

# Part 1.
# file_path = os.path.join(curr_dir, "data.txt")
file_path = os.path.join(curr_dir, "test.txt")
# file_path = os.path.join(curr_dir, "test_2.txt")

p1_list, p2_list = load_hands(file_path)

# print(p1_list, p2_list)
# print(play_simple_game(p1_list.copy(), p2_list.copy()))

# Part 2.
# file_path = os.path.join(curr_dir, "data.txt")
# file_path = os.path.join(curr_dir, "test.txt")
file_path = os.path.join(curr_dir, "test_2.txt")

p1_list, p2_list = load_hands(file_path)

print(p1_list, p2_list)
play_recursive_game(p1_list.copy(), p2_list.copy())