import os
import pandas as pd

curr_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(curr_dir, "data.txt"), header=None)

# Part 1.
seat_id_max = 0
seat_id_list = []

for _, row in df.iterrows():
    row_list = list(range(128))

    for letter in row[0][:7]:
        list_length = len(row_list)

        if letter == "F":
            row_list = row_list[: int(list_length / 2)]
        else:
            row_list = row_list[int(list_length / 2) :]

    col_list = list(range(8))

    for letter in row[0][7:]:
        list_length = len(col_list)

        if letter == "R":
            col_list = col_list[int(list_length / 2) :]
        else:
            col_list = col_list[: int(list_length / 2)]

    seat_id = row_list[0] * 8 + col_list[0]
    seat_id_list.append(seat_id)

print("Part 1:")
print(f"Highest seat ID: {max(seat_id_list)}\n")


# Part 2.
seat_id_min = min(seat_id_list)
seat_id_max = max(seat_id_list)

full_seat_list = range(seat_id_min, seat_id_max + 1)

print("Part 2:")

for seat in full_seat_list:
    if not seat in seat_id_list:
        print(f"Missing seat: {seat}")
