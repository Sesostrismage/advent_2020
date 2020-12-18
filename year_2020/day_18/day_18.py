import os
import re

def atomize(exp):
    for idx, item in enumerate(exp.split()):
        pass

def evaluate(expr):
    number = None
    operator = None
    expr_list = expr.split()

    for item in expr_list:
        if item in ['+', '*']:
            operator = item
        elif operator is None:
            number = int(item)
        elif operator == '+':
            number += int(item)
            operator = None
        elif operator == '*':
            number *= int(item)
            operator = None

    return number


curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "data.txt"))
# f = open(os.path.join(curr_dir, "test_part_1.txt"))
txt = f.readlines()
f.close()

txt_cleaned = [item.strip() for item in txt]
txt_cleaned = ['1 + 2 * 3 + 4 * 5 + 6']
# txt_cleaned = [
#     '1 + 2 * 3 + 4 * 5 + 6',
#     '1 + (2 * 3) + (4 * (5 + 6))',
#     '2 * 3 + (4 * 5)',
#     '5 + (8 * 3 + 9 + 3 * 4 * 3)',
#     '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
# ]

print(txt_cleaned)

num = evaluate(txt_cleaned[0])
print(num)