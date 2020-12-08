import os
import pandas as pd

curr_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(
    os.path.join(curr_dir, "data.txt"),
    sep=' ',
    header=None
)

print(df.head())

def run_code(code_set):
    idx = 0
    existing_idx_list = []
    acc = 0

    while True:
        if idx in existing_idx_list:
            status = 'loop'
            break
        elif idx > code_set.index[-1]:
            status = 'terminated'
            break

        else:
            existing_idx_list.append(idx)
            code = code_set.iloc[idx, 0]
            value = code_set.iloc[idx, 1]

            if code == 'acc':
                idx += 1
                acc += value
            elif code == 'jmp':
                idx += value
            elif code == 'nop':
                idx += 1
            else:
                print(f"Wrong instruction! {code}")
                break

    return acc, status

# Part 1.
a, s = run_code(df)

print(f"Acc value: {a}, status: {s}")
