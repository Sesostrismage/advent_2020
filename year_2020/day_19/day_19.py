import os

curr_dir = os.path.dirname(os.path.abspath(__file__))

# f = open(os.path.join(curr_dir, "data.txt"))
f = open(os.path.join(curr_dir, "test_1.txt"))
txt = f.readlines()
f.close()

txt_cleaned = [item.strip() for item in txt]
print(txt_cleaned)

rule_dict = {}

for line in txt_cleaned:
    rule_num = int(line.split(':')[0])
    rule_str = line.split(':')[1]
    if 'a' in rule_str or 'b' in rule_str:
        val = rule_str.strip(' "')
    elif '|' in rule_str:
        val = [
            [int(item) for item in rule_str.split('|')[0].split()],
            [int(item) for item in rule_str.split('|')[1].split()]
        ]
    else:
        val = rule_str.split()


    rule_dict[rule_num] = val

print(rule_dict)