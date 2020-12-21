import os

curr_dir = os.path.dirname(os.path.abspath(__file__))

# f = open(os.path.join(curr_dir, "data.txt"))
f = open(os.path.join(curr_dir, "test.txt"))
# f = open(os.path.join(curr_dir, "test_2.txt"))
txt = f.readlines()
f.close()

txt_cleaned = [item.strip() for item in txt]
print(txt_cleaned)

def get_possible_allergens_dict(l):
    fad = {}
    for item in l:
        breakdown = item.strip(')').split('(contains')
        for entry in breakdown[1].split():
            allergen = entry.strip(' ,')
            if not allergen in fad:
                fad[allergen] = [breakdown[0].split()]
            else:
                fad[allergen].append(breakdown[0].split())

    pad = {a: {} for a in fad}

    for key in fad:
        for idx, item in enumerate(fad[key]):
            if idx == 0:
                allergen_set = set(item)
            else:
                allergen_set = allergen_set & set(item)

        pad[key] = list(allergen_set)

    change = True
    remove_list = []

    while True:
        if change == False:
            break

        change = False

        for key in pad:
            if isinstance(pad[key], list) & len(pad[key]) == 1:
                pad[key] = pad[key][0]
                remove_list.append(pad[key])
                change = True
            elif isinstance(pad[key], list):
                for remove_item in remove_list:
                    if remove_item in pad[key]:
                        pad[key].remove(remove_item)


    return pad

allergen_dict = get_possible_allergens_dict(txt_cleaned)
print(allergen_dict)
