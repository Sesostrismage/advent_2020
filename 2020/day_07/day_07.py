import os

curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "data.txt"))
txt = f.readlines()
f.close()

txt_cleaned = [item.strip() for item in txt]

# print(txt_cleaned)

# part 1
rule_dict = {}

for rule in txt_cleaned:
    split_list = rule.split('contain')

    content_list = split_list[1].strip().split(', ')
    # print(content_list)

    bag = split_list[0][:-5]

    rule_dict[bag] = []

    for content in content_list:
        # print(content)

        if content == 'no other bags.':
            quantity = 0
            color = None
        else:
            content_split = content.split()
            quantity = int(content_split[0])
            color = f"{content_split[1]} {content_split[2]}"
        rule_dict[bag].append({'quantity': quantity, 'color': color})

print(rule_dict)
