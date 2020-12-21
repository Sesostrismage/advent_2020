import itertools
import os

curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "data.txt"))
# f = open(os.path.join(curr_dir, "test_1.txt"))
# f = open(os.path.join(curr_dir, "test_2.txt"))
txt = f.readlines()
f.close()

txt_cleaned = [item.strip() for item in txt]
# print(txt_cleaned)

rule_dict = {}
state = 'rules'
check_list = []

for line in txt_cleaned:
    if line == '':
        state = 'checks'

    elif state == 'rules':
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

    elif state == 'checks':
        check_list.append(line)

# print(rule_dict)

class RuleRoot:
    def __init__(self, rd):
        self.rd = rd
        self.base_rule = []

        for r in self.rd[0]:
            self.base_rule.append(RuleNode(self.rd, r))

    def yield_str(self):
        temp_list = []
        for node in self.base_rule:
            temp_list.append(node.yield_str())

        iter_list = list(itertools.product(*temp_list))
        out_list = ["".join(item) for item in iter_list]

        return out_list


class RuleNode:
    def __init__(self, rd, r_key):
        self.rd = rd
        self.node_rule = None
        self.node_type = None

        rule_val = self.rd[r_key]

        if isinstance(rule_val, str):
            self.node_rule = rule_val
            self.node_type = 'str'
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

    def yield_str(self):
        if self.node_type == 'str':
            out_list = [self.node_rule]
        elif self.node_type == 'linear':
            temp_list = []
            for node in self.node_rule:
                temp_list.append(node.yield_str())

            iter_list = list(itertools.product(*temp_list))
            out_list = ["".join(item) for item in iter_list]
        elif self.node_type == 'split':
            out_list = []

            for i in self.node_rule:
                temp_list = []
                for node in self.node_rule[i]:
                    temp_list.append(node.yield_str())

                iter_list = list(itertools.product(*temp_list))
                out_list += ["".join(item) for item in iter_list]

        return out_list

rr = RuleRoot(rule_dict)
# print(rr.base_rule)
str_list = rr.yield_str()
# print(str_list)

match_count = 0

for line in check_list:
    if line in str_list:
        match_count += 1

print(match_count)