import copy
import os
import datetime

curr_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(curr_dir, "test_input_1_day_16.txt")

with open(input_path, "r") as f:
    puzzle_input = f.readline()

bin_str = str(bin(int(puzzle_input, 16)))[2:]
print(bin_str)


class Packet:
    def __init__(self, string) -> None:
        self.packet_version = int(string[:3], 2)
        self.packet_type_id = int(string[3:6], 2)

        if self.packet_type_id == 4:
            self.type = "literal"

            idx = 6
            self.num_str = ""

            while True:
                self.num_str += string[idx + 1 : idx + 5]

                if string[idx] == "0":
                    break

                idx += 5

            self.num = int(self.num_str, 2)
            print(self.num_str)
            print(self.num)
        elif self.packet_type_id == 6:
            self.type = "operator"
            self.length_type_id = string[6]
            print(f"Length type ID: {self.length_type_id}")

            if self.length_type_id == "0":
                self.sub_packet_length_str = string[7:22]
                self.sub_packet_length = int(string[7:22], 2)
                print(self.sub_packet_length_str)
                print(self.sub_packet_length)

        print(f"Packet version: {self.packet_version}")
        print(f"Packet type ID: {self.packet_type_id}")


packet = Packet(bin_str)
