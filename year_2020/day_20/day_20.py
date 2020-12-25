import os
import pandas as pd

class tile:
    def __init__(self, lines):
        self.id = int(lines[0].split()[1].strip(':'))

        lines.pop(0)
        self.df = pd.DataFrame.from_records(lines)
        self.flip = None
        self.rotation = 0


curr_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(curr_dir, "data.txt")
file_path = os.path.join(curr_dir, "test.txt")
f = open(file_path)
txt = f.readlines()
f.close()

txt_cleaned = [line.strip() for line in txt]
txt_cleaned.append('')

print(txt_cleaned)

tile_list = []

temp_txt =[]

for line in txt_cleaned:
    if len(line) > 0:
        temp_txt.append(line)
    else:
        tile_list.append(tile(temp_txt))
        temp_txt = []


print(len(tile_list))