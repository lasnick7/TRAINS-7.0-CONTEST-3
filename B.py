N = int(input())
matrix = []
for _ in range(N):
    row = [int(x) for x in input().split()]
    matrix.append(row)
    
result = []

for i in range(N):
    element = 0
    for j in range(N):
        if i != j:
            element |= matrix[i][j]
    
    result.append(element)

print(*result)
