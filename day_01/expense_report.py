import datetime
import os
import pandas as pd

curr_dir = os.path.dirname(os.path.abspath(__file__))
df_1 = pd.read_csv(os.path.join(curr_dir, "data.txt"), header=None)

t_start = datetime.datetime.now()

# First part of problem.
for idx_1, row_1 in df_1.iterrows():
    df_2 = df_1[row_1[0] + df_1[0] == 2020]

    if len(df_2) > 0:
        print(row_1[0], df_2.iloc[0, 0])
        print(row_1[0] * df_2.iloc[0, 0])
        break

t_end = datetime.datetime.now()
print('Part 1 time:', t_end - t_start)


# Second part of problem.
t_start = datetime.datetime.now()

found = False

for idx_1, row_1 in df_1.iterrows():
    if found:
        break

    df_2 = df_1.loc[idx_1:].copy()
    df_2 = df_2[df_2[0] < 2020 - row_1[0]]

    for idx_2, row_2 in df_2.iterrows():
        if found:
            break

        df_3 = df_2.loc[idx_2:].copy()
        df_3 = df_3[df_3[0] == 2020 - row_1[0] - row_2[0]]

        if len(df_3) > 0:
            found = True
            print(row_1[0], row_2[0], df_3.iloc[0, 0])
            print(row_1[0] * row_2[0] * df_3.iloc[0, 0])
            break

t_end = datetime.datetime.now()
print('Part 2 time:', t_end - t_start)
