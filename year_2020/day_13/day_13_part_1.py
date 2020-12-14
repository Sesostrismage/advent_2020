import os

curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "data.txt"))
# f = open(os.path.join(curr_dir, "test.txt"))
txt = f.readlines()
f.close()

# print(txt)

timestamp = int(txt[0].strip())
print(timestamp)

bus_line_list = []

for item in txt[1].split(','):
    if item != 'x':
        bus_line_list.append(int(item))

print(bus_line_list)

min_time = 10000
best_bus = None

for bus in bus_line_list:
    number_departures = timestamp // bus
    waiting_time = (number_departures + 1) * bus - timestamp

    if waiting_time < min_time:
        min_time = waiting_time
        best_bus = bus

print(f"Best bus: {best_bus}")
print(f"Waiting time: {min_time}")
print(f"Result: {best_bus * min_time}")