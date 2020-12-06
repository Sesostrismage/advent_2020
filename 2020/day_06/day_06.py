import os

curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "data.txt"))
txt = f.readlines()
f.close()

txt_cleaned = [item.strip() for item in txt]
txt_cleaned.append('')

# Part 1.
answers_list = []
group_count = 0

for item in txt_cleaned:
    if len(item) > 0:
        for letter in item:
            if not letter in answers_list:
                answers_list.append(letter)
    else:
        group_count += len(answers_list)
        answers_list = []

print(f"Part 1 count: {group_count}")


# Part 2.
answers_set = None
group_count = 0

for item in txt_cleaned:
    if len(item) > 0 and answers_set is None:
        answers_set = set(list(item))
    elif len(item) > 0:
        answers_set = answers_set & set(list(item))
    else:
        group_count += len(answers_set)
        answers_set = None

print(f"Part 2 count: {group_count}")
