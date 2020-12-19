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
        val = [int(item) for item in rule_str.split()]


    rule_dict[rule_num] = val

print(rule_dict)

class RuleRoot:
    def __init__(self, rd):
        self.rd = rd
        self.base_rule = []

        for r in self.rd[0]:
            self.base_rule.append(RuleNode(self.rd, r))

class RuleNode:
    def __init__(self, rd, r_key):
        self.rd = rd
        self.node_rule = None
        self.node_type = None

        rule_val = self.rd[r_key]

        if isinstance(rule_val, str):
            self.node_rule = r_key
            self.node_type = 'end'
        else:
            if isinstance(rule_val[0], int):
                self.node_rule = []
                self.node_type = 'linear'
                for i in rule_val:
                    self.node_rule.append(RuleNode(self.rd, i))
            else:
                self.node_rule = {}

                for n in range(2):
                    self.node_rule[n] = []
                    self.node_type = 'split'

                    for s in rule_val[n]:
                        self.node_rule[n].append(RuleNode(self.rd, s))

rr = RuleRoot(rule_dict)
