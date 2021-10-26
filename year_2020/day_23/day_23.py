def cup_game(cl, number_moves=100):
    cc_idx = 0
    cc_label = cl[cc_idx]

    for n in range(number_moves):
        print(n, end="\r")
        # Pick up cups.
        pickup_list = []

        for _ in range(3):
            if cc_idx + 1 < len(cl):
                pickup_list.append(cl.pop(cc_idx + 1))
            else:
                pickup_list.append(cl.pop(0))

        # Select destination cup.
        destination_cup_label = cc_label - 1

        while True:
            if destination_cup_label in cl:
                break
            elif destination_cup_label < min(cl):
                destination_cup_label = max(cl)
                break
            else:
                destination_cup_label -= 1

        destination_cup_idx = cl.index(destination_cup_label)

        # Place picked-up cups.
        cl = cl[: destination_cup_idx + 1] + pickup_list + cl[destination_cup_idx + 1 :]

        # Re-find the current cup index.
        cc_idx = cl.index(cc_label)

        # Select new current cup.
        cc_idx = (cc_idx + 1) % len(cl)
        cc_label = cl[cc_idx]

    return cl, cc_label


# # Part 1.
# cup_list = [5, 3, 8, 9, 1, 4, 7, 6, 2]
# cup_list = cup_game(cup_list)
# # Collect final string.
# one_idx = cup_list.index(1)
# final_list = cup_list[one_idx +1:] + cup_list[:one_idx]
# final_list_as_str = [str(item) for item in final_list]
# final_str = ''.join(final_list_as_str)
# print(final_str)

# Part 2.
cup_list = [5, 3, 8, 9, 1, 4, 7, 6, 2] + list(range(10, 1000000 + 1))
cup_list, current_cup_label = cup_game(cup_list.copy(), number_moves=10000000)
current_cup_idx = cup_list.index(current_cup_label)
cup_one_idx = cup_list.index(1)
result = cup_list[cup_one_idx + 1] * cup_list[cup_one_idx + 2]
print(result)
