import sys

def pack():
    input_string = sys.stdin.readline().strip()
    code_dict = {chr(ord('a') + i): i for i in range(26)}
    next_code = 26
    width = 5
    max_code = 1 << width

    bit_buffer = 0
    bits_in_buffer = 0
    res = []

    word = ''
    for char in input_string :
        new_word = word + char
        
        if new_word in code_dict:
            word = new_word
            
        else:
            code = code_dict[word]
            bit_buffer = (bit_buffer << width) | code
            bits_in_buffer += width
            
            while bits_in_buffer >= 8:
                bits_in_buffer -= 8
                res.append((bit_buffer >> bits_in_buffer) & 0xFF)
                
            code_dict[new_word] = next_code
            next_code += 1
            
            if next_code == max_code:
                width += 1
                max_code = 1 << width
                
            word = char

    if word:
        code = code_dict[word]
        bit_buffer = (bit_buffer << width) | code
        bits_in_buffer += width
        
        while bits_in_buffer >= 8:
            bits_in_buffer -= 8
            res.append((bit_buffer >> bits_in_buffer) & 0xFF)
            
    if bits_in_buffer > 0:
        res.append((bit_buffer << (8 - bits_in_buffer)) & 0xFF)

    print(len(res))
    print(' '.join(str(x) for x in res), flush=True)

def unpack():
    def read():
        nonlocal bit_buffer, bits_in_buffer, index, width
        
        while bits_in_buffer < width and index < n:
            bit_buffer = (bit_buffer << 8) | data[index]
            bits_in_buffer += 8
            index += 1
            
        if bits_in_buffer < width:
            return None
        
        bits_in_buffer -= width
        code = (bit_buffer >> bits_in_buffer) & ((1 << width) - 1)
        bit_buffer &= (1 << bits_in_buffer) - 1
        
        return code
    
    n = int(sys.stdin.readline().strip())
    data = list(map(int, sys.stdin.readline().split()))
    code_dict = {i: chr(ord('a') + i) for i in range(26)}
    next_code = 26
    width = 5
    max_code = 1 << width

    bit_buffer = 0
    bits_in_buffer = 0
    index = 0

    first = read()
    prev = code_dict[first]
    res = [prev]

    while True:
        if next_code == max_code - 1:
            width += 1
            max_code = 1 << width

        code = read()
        if code is None:
            break
        
        if code in code_dict:
            entry = code_dict[code]
        else:
            entry = prev + prev[0]

        res.append(entry)
        code_dict[next_code] = prev + entry[0]
        next_code += 1
        prev = entry

    print(''.join(res), flush=True)
    
query = sys.stdin.readline().strip()
if query == 'pack':
    pack()
else:
    unpack()
