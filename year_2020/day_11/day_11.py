import numpy as np
import os
import pandas as pd

curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "data.txt"))
# f = open(os.path.join(curr_dir, "test_part_1.txt"))
txt = f.readlines()
f.close()

txt_cleaned = [item.strip() for item in txt]
txt_split = [list(item) for item in txt_cleaned]
df = pd.DataFrame.from_records(txt_split).replace({'L': 0, '.': np.nan})

# print(df)

df_count = df.copy()
df_prev = df.copy()
c = 1

print(f"Initial number of seats: {df.notnull().sum().sum()}")

while True:
    # df.to_excel(f"C:/Kode/advent_of_code/year_2020/day_11/df_{c}.xlsx")
    # df_count.to_excel(f"C:/Kode/advent_of_code/year_2020/day_11/df_count_{c}.xlsx")
    max_row = df.shape[0]
    max_col = df.shape[1]

    print(f"\nIteration {c}")

    for i, row in df.iterrows():
        for j, item in row.iteritems():
            local_sum = df.iloc[
                max(0, i-1):min(i+2, max_row),
                max(0, j-1):min(j+2, max_col)
            ].sum().sum() - df.iloc[i, j]
            df_count.iloc[i, j] = local_sum

    for i, row in df_count.iterrows():
        for j, item in row.iteritems():
            if df.iloc[i, j] == 0 and df_count.iloc[i, j] == 0:
                df.iloc[i, j] = 1
            elif df.iloc[i, j] == 1 and df_count.iloc[i, j] >= 4:
                df.iloc[i, j] = 0

    print(f"{df.sum().sum()} occupied seats.")

    if df.equals(df_prev):
        break
    else:
        df_prev = df.copy()
        c += 1

print(f"{df.sum().sum()} occupied seats.")
