import os
import pandas as pd

curr_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(curr_dir, "puzzle_input_day_03.txt")

with open(input_path, "r") as f:
    puzzle_input = f.readlines()

puzzle_input = [[sub_item for sub_item in item.strip()] for item in puzzle_input]
puzzle_df = pd.DataFrame.from_records(puzzle_input)

# Part 1.
gamma_rate = ""
epsilon_rate = ""

for col in puzzle_df.columns:
    vc = puzzle_df[col].value_counts()
    gamma_rate += vc.idxmax()
    epsilon_rate += vc.idxmin()

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)
print(f"Part 1: {gamma_rate * epsilon_rate}")


# Part 2.
def bit_criteria(df: pd.DataFrame, system: str) -> int:
    col_list = df.columns
    rating_df = df.copy()

    for col in col_list:
        vc = rating_df[col].value_counts()

        if len(vc) == 1:
            val = vc.index[0]
        elif system == "og":
            if vc.loc["1"] >= vc.loc["0"]:
                val = "1"
            else:
                val = "0"
        elif system == "co2":
            if vc.loc["0"] <= vc.loc["1"]:
                val = "0"
            else:
                val = "1"

        rating_df = rating_df[rating_df[col] == val]

        if len(rating_df) == 1:
            rating_str = "".join([rating_df.iloc[0, idx] for idx in rating_df.columns])
            rating = int(rating_str, 2)
            break

    return rating


# Oxygen generator rating.
og_rating = bit_criteria(puzzle_df, "og")
# CO2 scrubber rating.
co2_rating = bit_criteria(puzzle_df, "co2")

print(f"Part 2: {og_rating * co2_rating}")
