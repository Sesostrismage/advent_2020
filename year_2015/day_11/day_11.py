import pandas as pd


class Password:
    def __init__(self, pw: str) -> None:
        self.pw = pd.Series(index=range(len(pw)), dtype=int)
        for idx, char in enumerate(reversed(pw)):
            self.pw.loc[idx] = ord(char) - ord("a")

        self.forbidden_chars = [ord(char) - ord("a") for char in ["i", "o", "l"]]

    def increment(self):
        idx = 0

        while True:
            self.pw.loc[idx] += 1

            if self.pw.loc[idx] in self.forbidden_chars:
                self.pw.loc[idx] += 1

            if self.pw.loc[idx] > 25:
                self.pw.loc[idx] = 0
                idx += 1
            else:
                break

    def to_chars(self):
        out_str = ""

        for _, num in self.pw.iteritems():
            out_str += chr(num + ord("a"))

        return out_str[::-1]

    def rule_1(self):
        return (
            (self.pw == self.pw.shift(-1) + 1) & (self.pw == self.pw.shift(-2) + 2)
        ).any()

    def rule_3(self):
        pairs = self.pw == self.pw.shift(-1)
        diff_pairs = len(self.pw.loc[pairs].value_counts()) > 1
        return diff_pairs


password = Password("cqjxjnds")

# Part 1.
while True:
    password.increment()
    if password.rule_1() and password.rule_3():
        print(f"Part 1: {password.to_chars()}")
        password = Password(password.to_chars())
        break

# Part 2.
while True:
    password.increment()
    if password.rule_1() and password.rule_3():
        print(f"Part 2: {password.to_chars()}")
        break
