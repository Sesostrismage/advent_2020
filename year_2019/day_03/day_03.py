import os
import pandas as pd

class Circuit:
    def __init__(self, w1, w2):
        self.wire_1 = w1
        self.wire_2 = w2
        self.center = 5000
        self.circuit = pd.DataFrame(False, index=range(self.center*2), columns=range(self.center*2))
        self.shortest_distance = self.center * 2

    def run_wires(self):
        # Run wire 1.
        x = self.center
        y = self.center

        for step in self.wire_1:
            d = step[0]
            l = int(step[1:])

            if d == 'R':
                self.circuit.iloc[x+1:x+l+1, y] = True
                x += l
            elif d == 'L':
                self.circuit.iloc[x-l:x, y] = True
                x -= l
            elif d == 'U':
                self.circuit.iloc[x, y+1:y+l+1] = True
                y += l
            elif d == 'D':
                self.circuit.iloc[x, y-l:y] = True
                y -= l

        # Run wire 2.
        x = self.center
        y = self.center

        for step in self.wire_2:
            d = step[0]
            l = int(step[1:])

            if d == 'R':
                for _ in range(l):
                    x += 1
                    self.check_intersection(x, y)
            elif d == 'L':
                for _ in range(l):
                    x -= 1
                    self.check_intersection(x, y)
            elif d == 'U':
                for _ in range(l):
                    y += 1
                    self.check_intersection(x, y)
            elif d == 'D':
                for _ in range(l):
                    y -= 1
                    self.check_intersection(x, y)

        return self.shortest_distance

    def check_intersection(self, x, y):
        if self.circuit.iloc[x, y] == True:
            local_distance = abs(x - self.center) + abs(y - self.center)

            if local_distance < self.shortest_distance:
                self.shortest_distance = local_distance

curr_dir = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(curr_dir, "data.txt"))
wire_1_raw = f.readline()
wire_2_raw = f.readline()
f.close()

wire_1 = wire_1_raw.split(',')
wire_2 = wire_2_raw.split(',')

circuit = Circuit(wire_1, wire_2)
shortest_distance = circuit.run_wires()
print(shortest_distance)