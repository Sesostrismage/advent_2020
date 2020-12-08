class IntCode:
    def __init__(self, code):
        self.code_in = code.copy()
        self.code_out = code.copy()
        self.status = None

    def run_code(self):
        idx = 0

        while True:
            if idx > len(self.code_out) + 1:
                self.status = 'out_of_bounds'
                break
            # Addition.
            elif self.code_out[idx] == 1:
                in_1_idx = self.code_out[idx+1]
                in_2_idx = self.code_out[idx+2]
                out_idx = self.code_out[idx+3]
                self.code_out[out_idx] = self.code_out[in_1_idx] + self.code_out[in_2_idx]
            # Multiplication.
            elif self.code_out[idx] == 2:
                in_1_idx = self.code_out[idx+1]
                in_2_idx = self.code_out[idx+2]
                out_idx = self.code_out[idx+3]
                self.code_out[out_idx] = self.code_out[in_1_idx] * self.code_out[in_2_idx]
            # Termination.
            elif self.code_out[idx] == 99:
                self.status = 'termintated'
                break

            idx += 4
