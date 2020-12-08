import os
import pandas as pd

curr_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(
    os.path.join(curr_dir, "data.txt"),
    sep=' ',
    header=None,
    names=['limits', 'letter', 'code']
)
df['letter'] = df['letter'].str.replace(':', '')
df[['min', 'max']] = df['limits'].str.split('-', expand=True)

# First part of problem.
total = 0

for _, row in df.iterrows():
    if int(row['min']) <= row['code'].count(row['letter']) <= int(row['max']):
        total += 1

print(df.head())
print(total)


# Second part of problem.
total = 0
for _, row in df.iterrows():
    if (
        bool(row['code'][int(row['min'])-1] == row['letter'])
        != bool(row['code'][int(row['max'])-1] == row['letter'])
    ):
        total += 1

print(total)
