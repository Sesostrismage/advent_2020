import pandas as pd
import os

curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "data.txt"))
txt = f.readlines()
f.close()

txt = ['','67,7,59,61']

bus_df = pd.DataFrame()

c = 0
c_abs = 0

for bus in txt[1].split(','):
    if bus != 'x' and bus == txt[1].split(',')[0]:
        bus_df = pd.concat([
            bus_df,
            pd.DataFrame({'Bus': [int(bus)], 'Offset': [c_abs]}, index=[int(bus)])
        ])
    elif bus != 'x':
        c_abs += 1
        bus_df = pd.concat([
            bus_df,
            pd.DataFrame({'Bus': [int(bus)], 'Offset': [c_abs]}, index=[int(bus)])
        ])
    else:
        c_abs += 1

max_bus = bus_df['Bus'].idxmax()

print(bus_df)

t = max_bus - bus_df['Offset'].loc[max_bus]

while True:
    test = (t + bus_df['Offset']).mod(bus_df['Bus'])

    if t > 100000000000000:
        print('Reached target area.')
    elif t > 1000000000000000:
        break
    elif test.min() == 0 and test.max() == 0:
        break
    else:
        t += max_bus

print(t)
