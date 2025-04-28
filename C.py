def rearrange():
    n = int(input())
    a = [int(x) for x in input().split()]

    length = max(x.bit_length() for x in a)
    ones = [bin(x).count('1') for x in a]
    total_ones = sum(ones)

    if total_ones % 2 == 1:
        print("impossible")
        return

    half_of_ones = total_ones // 2
    less_half = n // 2
    if half_of_ones > less_half * length:
        print("impossible")
        return

    bit_pares = [half_of_ones // length] * length
    for j in range(half_of_ones % length):
        bit_pares[j] += 1

    b = [0] * n
    rest = [*ones]

    for i in range(length):
        need = 2 * bit_pares[i]
        if need == 0:
            continue

        idxs = sorted(range(n), key=lambda x: rest[x], reverse=True)
        chosen = idxs[:need]

        if rest[chosen[-1]] == 0:
            print("impossible")
            return

        for j in chosen:
            b[j] |= (1 << i)
            rest[j] -= 1
    print(*b)
rearrange()
