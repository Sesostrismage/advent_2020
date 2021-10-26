class IntCode:
    def __init__(self, code, input_1, input_2):
        self.code_in = code.copy()
        self.memory = code.copy()
        self.memory[1] = input_1
        self.memory[2] = input_2
        self.status = None

    def run_code(self):
        pointer = 0

        while True:
            if pointer > len(self.memory) + 1:
                self.status = "out_of_bounds"
                break
            # Addition.
            elif self.memory[pointer] == 1:
                param_1_idx = self.memory[pointer + 1]
                param_2_idx = self.memory[pointer + 2]
                out_idx = self.memory[pointer + 3]
                self.memory[out_idx] = (
                    self.memory[param_1_idx] + self.memory[param_2_idx]
                )
                pointer += 4
            # Multiplication.
            elif self.memory[pointer] == 2:
                param_1_idx = self.memory[pointer + 1]
                param_2_idx = self.memory[pointer + 2]
                out_idx = self.memory[pointer + 3]
                self.memory[out_idx] = (
                    self.memory[param_1_idx] * self.memory[param_2_idx]
                )
                pointer += 4
            # Termination.
            elif self.memory[pointer] == 99:
                self.status = "termintated"
                break

        output = self.memory[0]

        return output
