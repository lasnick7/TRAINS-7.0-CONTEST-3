n = int(input())
bin_n = bin(n)[2:]
shifts = set()
curr_bin = bin_n
while True:
    shifts.add(curr_bin)
    last_char = curr_bin[-1]
    rest_chars = curr_bin[:-1]
    next_bin = last_char + rest_chars
    if next_bin == bin_n:
        break
    curr_bin = next_bin 
print(max(list(map(lambda x: int(x, 2), shifts))))
