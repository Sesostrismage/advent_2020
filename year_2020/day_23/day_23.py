#Test 1.
cup_list = [3, 8, 9, 1, 2, 5, 4, 6, 7]

def cup_game(cl, number_moves=100):
    current_cup_idx = 0
    current_cup_label = cl[current_cup_idx]

    for _ in range(number_moves):
        # Pick up cups.
        pickup_list = []

        for _ in range(3):
            if current_cup_idx + 1 < len(cl):
                pickup_list.append(cl.pop(current_cup_idx + 1))
            else:
                pickup_list.append(cl.pop(0))

        # Select destination cup.
        destination_cup_label = current_cup_label - 1

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
        cl = cl[:destination_cup_idx + 1] + pickup_list + cl[destination_cup_idx + 1:]

        # Select new current cup.
        current_cup_idx = (current_cup_idx + 1) % len(cl)
        current_cup_label = cl[current_cup_idx]

        print(cl)

cup_game(cup_list, number_moves=10)