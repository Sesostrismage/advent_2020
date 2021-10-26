import os

curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "data.txt"))
# f = open(os.path.join(curr_dir, "test.txt"))
# f = open(os.path.join(curr_dir, "test_2.txt"))
txt = f.readlines()
f.close()

txt_cleaned = [item.strip() for item in txt]
# print(txt_cleaned)


def get_ingredients(l):
    out_list = []

    for item in l:
        out_list.append(item.split(" (contains ")[0].split())

    return out_list


def get_possible_allergens_dict(l):
    fad = {}
    for item in l:
        breakdown = item.strip(")").split("(contains")
        for entry in breakdown[1].split():
            allergen = entry.strip(" ,")
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

    # print(pad)

    change = True

    while True:
        if change == False:
            break

        change = False

        for key in pad:
            if (isinstance(pad[key], list)) & (len(pad[key]) == 1):
                pad[key] = pad[key][0]
                remove_item = pad[key]

                change = True

                # Remove singular ingredient from all other keys.
                for remove_key in pad:
                    if (
                        isinstance(pad[remove_key], list)
                        and remove_item in pad[remove_key]
                    ):
                        pad[remove_key].remove(remove_item)

                break

    al = []

    for key in sorted(pad.keys()):
        if isinstance(pad[key], str):
            al.append(pad[key])
        else:
            al += pad[key]

    return pad, al


ingredient_list = get_ingredients(txt_cleaned)
# print(ingredient_list)
allergen_dict, allergen_list = get_possible_allergens_dict(txt_cleaned)
print(allergen_dict)
print(allergen_list)

non_allergen_count = 0

for ingredients in ingredient_list:
    non_allergen_count += len(
        [item for item in ingredients if item not in allergen_list]
    )

print(non_allergen_count)
dangerous_ingredient_string = ",".join(allergen_list)
print(dangerous_ingredient_string)
