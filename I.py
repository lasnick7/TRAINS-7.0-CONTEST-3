query = int(input())
data = input()
n = len(data)        

def encode(data, n):

    extra = 0
    while (1 << extra) < n + extra + 1:
        extra += 1
    m = n + extra

    coded_arr = ['0'] * m

    data_pointer = 0
    for index in range(1, m + 1):
        if not (index and (index & (index - 1)) == 0):
            coded_arr[index - 1] = data[data_pointer]
            data_pointer += 1

    for i in range(extra):
        bit = 1 << i
        mask = 0
        for j in range(1, m + 1):
            if j & bit and j != bit:
                mask ^= (coded_arr[j - 1] == '1')
        coded_arr[bit - 1] = '1' if mask else '0'

    return ''.join(coded_arr)

def decode(data, m):
    extra = 0
    while (1 << extra) < m + 1:
        extra += 1

    error = 0
    for i in range(extra):
        bit = 1 << i
        mask = 0
        for j in range(1, m + 1):
            if j & bit and j != bit:
                mask ^= (data[j - 1] == '1')
        if mask != (data[bit - 1] == '1'):
            error |= bit
            
    coded_arr = list(data)
    if 1 <= error <= m:
        index = error - 1
        coded_arr[index] = '0' if coded_arr[index] == '1' else '1'

    decoded_arr = []
    for index in range(1, m + 1):
        if not (index and (index & (index - 1)) == 0):
            decoded_arr.append(coded_arr[index - 1])
    return ''.join(decoded_arr)

if query == 1:
    print(encode(data, n))
else:
    print(decode(data, n))
