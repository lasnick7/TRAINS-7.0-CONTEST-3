N, K = [int(x) for x in input().split()]
arr = [0] * N
fenvic = [0] * N

def update(index, x):
    curr_i = index
    while curr_i < N:
        fenvic[curr_i] -= arr[index]
        fenvic[curr_i] += x
        curr_i |= (curr_i + 1)
    arr[index] = x

def find_sum_from_0(r):
    curr_i = r
    curr_sum = 0
    while curr_i >= 0:
        curr_sum += fenvic[curr_i]
        curr_i &= curr_i + 1
        curr_i -= 1
    return curr_sum

ans = []
for _ in range(K):
    q, x, y = [x for x in input().split()]
    if q == 'A':
        update(int(x) - 1, int(y))
    else:
        sumX = find_sum_from_0(int(x) - 2)
        sumY = find_sum_from_0(int(y) - 1)
        ans.append(sumY - sumX)
        
for a in ans:
    print(a)
