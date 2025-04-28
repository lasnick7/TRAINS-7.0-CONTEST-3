import sys
input = sys.stdin.readline

n, k = [int(x) for x in input().split()]

mask = (1 << n) - 1

XZ = [0] * n
YZ = [0] * n

XY = [bytearray(n) for _ in range(n)]

for _ in range(k):
    x, y, z = [int(x) - 1 for x in input().split()]
    XY[x][y] = 1
    bit = 1 << z
    XZ[x] |= bit
    YZ[y] |= bit

not_covered_x = [x for x in range(n) if XZ[x] != mask]
not_covered_y = [y for y in range(n) if YZ[y] != mask]

for x in not_covered_x:
    mask_x = XZ[x]
    for y in not_covered_y:
        if XY[x][y]:
            continue
        cover = mask_x | YZ[y]
        if cover != mask:
            check = mask ^ cover
            z = check.bit_length() - 1
            print("NO")
            print(x + 1, y + 1, z + 1)
            sys.exit()
print("YES")
