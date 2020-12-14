import os

curr_dir = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(curr_dir, "data.txt"))
txt = f.readlines()
f.close()

# txt = ['', '67,x,7,59,61']

bus_list = []

counter = 0

for bus in txt[1].split(','):
    if bus != 'x':
        bus_list.append([int(bus), counter])

    counter += 1

print(bus_list)

for bus in bus_list:
    if bus == bus_list[0]:
        factor = bus[0]
        offset = bus[1]
    else:
        step = 1
        first_match = False

        while True:
            timestamp = step * factor + offset
            if  (
                (timestamp + bus[1]) % bus[0] == 0
                and bus == bus_list[-1]
            ):
                print(f"Success! {timestamp}")
                break
            elif  (timestamp + bus[1]) % bus[0] == 0:
                if first_match == False:
                    new_offset = timestamp
                    first_match = True
                    step += 1
                elif first_match == True:
                    new_factor = timestamp - new_offset
                    factor = new_factor
                    offset = new_offset
                    break
            else:
                step += 1

print(timestamp)