import os

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

def find_parentheses(expr):
    start_idx = 0
    end_idx = 0

    for idx, char in enumerate(expr):
        if char == '(':
            start_idx = idx
        elif char == ')':
            end_idx = idx
            break

    return start_idx, end_idx

def collapse_parentheses(expr):
    while True:
        if '(' in expr:
            start_idx, end_idx = find_parentheses(expr)
            expr = expr[:start_idx] + str(evaluate(expr[start_idx+1:end_idx])) + expr[end_idx+1:]
        else:
            break

    number = evaluate(expr)

    return number


curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "data.txt"))
txt = f.readlines()
f.close()

txt_cleaned = [item.strip() for item in txt]

total = 0

for item in txt_cleaned:
    print(item)
    num = collapse_parentheses(item)
    total += num

print(f"Part 1 sum: {total}")
