n = int(input())
matrix = [[0]*n for i in range(n)]
cnt = 0
total = 0

for i in range(0, n):
    for j in range(0, n):
        cnt += 1
        matrix[i][j] = cnt

for i in range(0, n):
    total += matrix[0][i]
for i in range(1, n):
    total += matrix[i][n-1]
for i in range(n-2, -1, -1):
    total += matrix[n-1][i]
for i in range(n-2, 0, -1):
    total += matrix[i][0]

print(total)
