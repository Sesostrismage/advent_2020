import os
import pandas as pd

curr_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(
    os.path.join(curr_dir, "data.txt"),
    header=None
)
series = df[0]

series = pd.Series([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4])
# series = pd.Series([28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49,
#     45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3
# ])

# print(series)

# Part 1.
def chain(adapter_series):
    series_sorted = pd.concat(
        [
            pd.Series([0]),
            adapter_series.sort_values(),
            pd.Series([adapter_series.max() + 3])
        ]
    )
    # print(series_sorted)
    series_diff = series_sorted.diff()
    # print(series_diff)
    value_counts = series_diff.value_counts()
    print(f"Part 1 answer: {value_counts.iloc[0] * value_counts.iloc[-1]}")

chain(series)