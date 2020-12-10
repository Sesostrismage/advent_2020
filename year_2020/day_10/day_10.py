import datetime
import os
import pandas as pd

curr_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(
    os.path.join(curr_dir, "data.txt"),
    header=None
)
series = df[0]

# series = pd.Series([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4])
# series = pd.Series([28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49,
#     45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3
# ])

time_start = datetime.datetime.now()

def count_combinations(sequence):
    comb_list = [[sequence[0]]]

    for item in sequence:
        if item == sequence[0]:
            new_comb_list = comb_list.copy()
        else:
            new_comb_list = comb_list.copy()

            for comb in comb_list:
                if item - comb[-1] <= 3:
                    new_comb_list.append(comb.copy() + [item])
                else:
                    new_comb_list.append(comb.copy())

        comb_list = new_comb_list

    valid_combinations = 0

    for item in comb_list:
        if item[-1] == sequence[-1]:
            valid_combinations += 1

    return valid_combinations


def chain(adapter_series):
    series_sorted = pd.concat(
        [
            pd.Series([0]),
            adapter_series.sort_values(),
            pd.Series([adapter_series.max() + 3])
        ]
    ).reset_index(drop=True)
    series_diff = series_sorted.diff()

    # Part 1.
    value_counts = series_diff.value_counts()
    print(f"Part 1 answer: {value_counts.iloc[0] * value_counts.iloc[-1]}")

    # Part 2.
    junction_series = series_sorted[(series_diff == 3) | (series_diff.shift(-1) == 3)]

    prev_idx = 0
    total_combinations = 1

    for idx in junction_series.index:
        junction_list = list(series_sorted.iloc[prev_idx:idx+1])

        junction_combinations = count_combinations(junction_list)
        total_combinations = total_combinations * junction_combinations

        prev_idx = idx

    print(f"Part 2 answer: {total_combinations}")

chain(series)

time_end = datetime.datetime.now()

print(f"Time elapsed: {time_end - time_start}")