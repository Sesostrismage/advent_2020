import os

curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "data.txt"))
# f = open(os.path.join(curr_dir, "test_part_2.txt"))
txt = f.readlines()
f.close()

txt_cleaned = [item.strip() for item in txt]

# print(txt_cleaned)

bag_rule_dict = {}

for line in txt_cleaned:
    rule_components = line.split('contain')
    own_color = rule_components[0][:-6]

    contains_list_input = rule_components[1].strip().split(', ')
    contains_list_output = []

    for content in contains_list_input:
    # print(content)

        if content == 'no other bags.':
            contains_list_output = None
        else:
            content_split = content.split()
            quantity = int(content_split[0])
            bag_color = f"{content_split[1]} {content_split[2]}"

            contains_list_output.append({'color': bag_color, 'quantity': quantity})

    bag_rule_dict[own_color] = contains_list_output


class bag:
    def __init__(self, color, rule_dict):
        self.own_color = color
        self.contains_list = []

        self.contains_list = rule_dict[color]

    def get_own_color(self):
        return self.own_color

    def fill_bag(self, rule_dict):
        if not self.contains_list is None:
            for item in self.contains_list:
                item['bag'] = bag(item['color'], rule_dict)
                item['bag'].fill_bag(rule_dict)

    def is_color_in_bag(self, color):
        answer = False

        if self.contains_list is None:
            pass
        else:
            for entry in self.contains_list:
                if entry['color'] == color:
                    answer = True

        if answer == False:
            if self.contains_list is None:
                pass
            else:
                for entry in self.contains_list:
                    if entry['bag'].is_color_in_bag(color):
                        answer = True
                        break

        return answer

    def number_bags_with_self(self):
        number = 1

        if self.contains_list is None:
            pass
        else:
            for entry in self.contains_list:
                number += entry['quantity'] * entry['bag'].number_bags_with_self()

        return number


bag_list = []

for bag_color in bag_rule_dict:
    # print(bag_color)
    bag_n = bag(bag_color, bag_rule_dict)
    bag_n.fill_bag(bag_rule_dict)
    bag_list.append(bag_n)

# Part 1.
number_bags = 0

for bag in bag_list:
    if bag.is_color_in_bag('shiny gold'):
        number_bags += 1

print(f"Number of bags containing shiny gold: {number_bags}")

# Part 2.

for bag in bag_list:
    if bag.get_own_color() == 'shiny gold':
        number_contained_bags = bag.number_bags_with_self()

print(f"Number of bags in shiny gold bag: {number_contained_bags -1}")