import os
import pandas as pd

curr_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(curr_dir, "puzzle_input_day_03.txt")

with open(input_path, "r") as f:
    puzzle_input = f.readlines()

puzzle_input = [[sub_item for sub_item in item.strip()] for item in puzzle_input]
df = pd.DataFrame.from_records(puzzle_input)
print(df)
print(df[0].value_counts())

gamma_rate = ""
epsilon_rate = ""

for col in df.columns:
    vc = df[col].value_counts()
    gamma_bit = vc.idxmax()
    gamma_rate += gamma_bit
    epsilon_bit = vc.idxmin()
    epsilon_rate += epsilon_bit

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)
print(gamma_rate * epsilon_rate)
