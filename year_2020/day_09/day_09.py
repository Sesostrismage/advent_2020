import os
import pandas as pd

curr_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(
    os.path.join(curr_dir, "data.txt"),
    header=None
)

# Part 1.
def find_pair(segment, target):
    answer = False

    for i, r in segment.copy().iterrows():
        pair = segment.copy().drop(i, axis=0)

        if target in (r[0] + pair[0]).values:
            answer = True
            break

    return answer

preamble = 25

for idx, row in df.iterrows():
    if idx < preamble:
        pass
    else:
        seg = df.iloc[idx-preamble:idx, :]
        invalid_number = row[0]

        if not find_pair(seg, invalid_number):
            print(f"Invalid number! {invalid_number}")
            break

# Part 2.
n = 2

while n < len(df):
    roll_sum = df[0].rolling(n).sum()
    if invalid_number in roll_sum.values:
        print(f"Found invalid sum! N = {n}")
        break

    n += 1

roll_sum.fillna(0, inplace=True)
sum_idx = (roll_sum[roll_sum == invalid_number]).index[0]
sum_segment = df[0].iloc[sum_idx-n+1:sum_idx+1]

print(f"Encyption weakness: {sum_segment.min() + sum_segment.max()}")
