import copy
import os
import datetime

curr_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(curr_dir, "test_input_2_day_16.txt")

with open(input_path, "r") as f:
    puzzle_input = f.readline()

bin_str = str(bin(int(puzzle_input, 16)))[2:]
len_bin_str = len(bin_str)
pad_size = 4 - len_bin_str % 4
bin_str = bin_str.zfill(len_bin_str + pad_size)
print(bin_str)


class Packet:
    def __init__(self, string, idx=0) -> None:
        self.packet_version = int(string[idx : idx + 3], 2)
        self.packet_type_id = int(string[idx + 3 : idx + 6], 2)
        self.idx = idx + 6

        while True:
            str_done = False
            if self.packet_type_id == 4:
                self.type = "literal"
                self.num_str = ""

                while True:
                    self.num_str += string[self.idx + 1 : self.idx + 5]

                    if string[self.idx] == "0":
                        str_done = True
                        break

                    self.idx += 5

                self.num = int(self.num_str, 2)
                print(self.num_str)
                print(self.num)

            elif self.packet_type_id == 6:
                self.type = "operator"
                self.length_type_id = int(string[idx], 2)
                self.idx += 1
                print(f"Length type ID: {self.length_type_id}")
                self.sub_packets = []

                if self.length_type_id == 0:
                    self.sub_packet_length_str = string[self.idx : self.idx + 15]
                    self.sub_packet_length = int(string[self.idx : self.idx + 15], 2)
                    print(f"Sub-packet length: {self.sub_packet_length}")
                    self.idx += 15

                    sub_packet = Packet(string, self.idx)
                    self.idx = sub_packet.get_idx()
                    self.sub_packets.append(sub_packet)
                    str_done = True

            if str_done:
                break

        print(f"Packet version: {self.packet_version}")
        print(f"Packet type ID: {self.packet_type_id}")

    def get_idx(self):
        return self.idx


packet = Packet(bin_str)
for sub_packet in packet.sub_packets:
    print(sub_packet.num)
