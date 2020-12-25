subject_number_door = 7
subject_number_card = 7

# Test values.
# public_key_card = 5764801
# public_key_door = 17807724

# Actual values.
public_key_card = 12232269
public_key_door = 19452773

def find_loop_size(sn, pk):
    divisor = 20201227
    value = 1
    ls = 1

    while True:
        value = (value * sn) % divisor

        if value != pk:
            ls += 1
        else:
            break

    return ls

def find_encryption_key(sn, ls):
    divisor = 20201227
    value = 1

    for n in range(ls):
        value = (value * sn) % divisor

    return value

loop_size_card = find_loop_size(subject_number_card, public_key_card)
print(loop_size_card)

loop_size_door = find_loop_size(subject_number_card, public_key_door)
print(loop_size_door)

print(find_encryption_key(public_key_door, loop_size_card))
print(find_encryption_key(public_key_card, loop_size_door))
