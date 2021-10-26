import numpy as np
import os
import pandas as pd

curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "data.txt"))
# f = open(os.path.join(curr_dir, "test.txt"))
txt = f.readlines()
f.close()

txt_cleaned = [item.strip() for item in txt]
txt_split = [list(item) for item in txt_cleaned]
df = pd.DataFrame.from_records(txt_split).replace({"L": 0, ".": np.nan})

# print(df)

df_count = df.copy()
df_prev = df.copy()
iteration = 1

print(f"Initial number of seats: {df.notnull().sum().sum()}")


def count_visible_seats(df_vis, r, c):
    visible_sum = 0

    dir_list = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

    for dir_pair in dir_list:
        m = r
        n = c

        while True:
            m += dir_pair[0]
            n += dir_pair[1]

            if (m not in df_vis.index) or (n not in df_vis.columns):
                break
            elif not np.isnan(df_vis.iloc[m, n]):
                visible_sum += df_vis.iloc[m, n]
                break

    return visible_sum


while True:
    # df.to_excel(f"C:/Kode/advent_of_code/year_2020/day_11/df_{c}.xlsx")
    # df_count.to_excel(f"C:/Kode/advent_of_code/year_2020/day_11/df_count_{c}.xlsx")
    max_row = df.shape[0]
    max_col = df.shape[1]

    print(f"\nIteration {iteration}")

    for i, row in df.iterrows():
        for j, item in row.iteritems():
            local_sum = count_visible_seats(df, i, j)
            df_count.iloc[i, j] = local_sum

    for i, row in df_count.iterrows():
        for j, item in row.iteritems():
            if df.iloc[i, j] == 0 and df_count.iloc[i, j] == 0:
                df.iloc[i, j] = 1
            elif df.iloc[i, j] == 1 and df_count.iloc[i, j] >= 5:
                df.iloc[i, j] = 0

    print(f"{df.sum().sum()} occupied seats.")

    if df.equals(df_prev):
        break
    else:
        df_prev = df.copy()
        iteration += 1

print(f"{df.sum().sum()} occupied seats.")
