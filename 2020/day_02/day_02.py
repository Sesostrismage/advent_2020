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

total = 0

for _, row in df.iterrows():
    if int(row['min']) <= row['code'].count(row['letter']) <= int(row['max']):
        total += 1

print(df.head())
print(total)
