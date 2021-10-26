import hashlib

# Part 1.
string = "iwrupvqb"
n = 0

while True:
    n += 1
    test_str = f"{string}{n}"
    result = hashlib.md5(test_str.encode())
    if result.hexdigest().startswith("00000"):
        print(f"Part 1 solution: {n}")
        break

# Part 2:
n = 0

while True:
    n += 1
    test_str = f"{string}{n}"
    result = hashlib.md5(test_str.encode())
    if result.hexdigest().startswith("000000"):
        print(f"Part 2 solution: {n}")
        break
