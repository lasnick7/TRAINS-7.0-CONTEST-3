n = int(input()) 
fenvic = [[[0] * (n) for _ in range(n)] for _ in range(n)]
q = [int(x) for x in input().split()]

def update(x, y, z, value):
    i = x
    while i < n:
        j = y
        while j < n:
            k = z
            while k < n:
                fenvic[i][j][k] += value
                k |= k + 1
            j |= j + 1
        i |= i + 1
        
def prefsum(x, y, z):
    ans = 0
    i = x
    while i >= 0:
        j = y
        while j >= 0:
            k = z
            while k >= 0:
                ans += fenvic[i][j][k]
                k = (k & (k + 1)) - 1
            j = (j & (j + 1)) - 1
        i = (i & (i + 1)) - 1
    return ans

def segsum(x1, y1, z1, x2, y2, z2):
    return prefsum(x2, y2, z2) - prefsum(x2, y2, z1 - 1) - prefsum(x2, y1 - 1, z2) - prefsum(x1 - 1, y2, z2) + prefsum(x1 - 1, y1 - 1, z2) + prefsum(x1 - 1, y2, z1 - 1) + prefsum(x2, y1 - 1, z1 - 1) - prefsum(x1 - 1, y1 - 1, z1 - 1)
    
ans = []           
while q[0] != 3:
    if q[0] == 1:
        x, y, z, k = q[1:]
        update(x, y, z, k)
    else:
        x1, y1, z1, x2, y2, z2 = q[1:]
        ans.append(segsum(x1, y1, z1, x2, y2, z2))
    
    q =  [int(x) for x in input().split()]
    
for a in ans:
    print(a)
