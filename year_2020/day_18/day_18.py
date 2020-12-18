import os

def evaluate_basic(expr):
    number = None
    operator = None
    expr_list = expr.split()

    for component in expr_list:
        if component in ['+', '*']:
            operator = component
        elif operator is None:
            number = int(component)
        elif operator == '+':
            number += int(component)
            operator = None
        elif operator == '*':
            number *= int(component)
            operator = None

    return number

def evaluate_advanced(expr):
    expr_list = expr.split()

    while True:
        if not '+' in expr_list:
            break
        else:
            new_expr = []
            number = None
            summing = False

            for component in expr_list:
                if component == '*':
                    new_expr.append(str(number))
                    new_expr.append(component)
                elif component == '+':
                    summing = True
                elif summing == False:
                    number = int(component)
                elif summing:
                    number += int(component)
                    summing = False

            new_expr.append(str(number))

        expr_list = new_expr

    result = 1
    operator = None

    for component in expr_list:
        if component == '*':
            operator = component
        elif operator is None:
            result = int(component)
        elif operator == '*':
            result *= int(component)
            operator = None

    return result

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

def collapse_parentheses_basic(expr):
    while True:
        if '(' in expr:
            start_idx, end_idx = find_parentheses(expr)
            expr = expr[:start_idx] + str(evaluate_basic(expr[start_idx+1:end_idx])) + expr[end_idx+1:]
        else:
            break

    number = evaluate_basic(expr)

    return number


def collapse_parentheses_advanced(expr):
    while True:
        if '(' in expr:
            start_idx, end_idx = find_parentheses(expr)
            expr = expr[:start_idx] + str(evaluate_advanced(expr[start_idx+1:end_idx])) + expr[end_idx+1:]
        else:
            break

    number = evaluate_advanced(expr)

    return number


curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "data.txt"))
txt = f.readlines()
f.close()
txt_cleaned = [item.strip() for item in txt]

# Part 1.
total = 0

for item in txt_cleaned:
    num = collapse_parentheses_basic(item)
    total += num

print(f"Part 1 sum: {total}")


# Part 2.
total = 0

for item in txt_cleaned:
    num = collapse_parentheses_advanced(item)
    total += num

print(f"Part 2 sum: {total}")
