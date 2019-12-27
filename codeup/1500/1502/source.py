n = int(input())
matrix = [[0]*n for i in range(n)]
cnt = 0

for i in range(0, n):
    for j in range(0, n):
        cnt += 1
        matrix[j][i] = cnt

for i in range(0, n):
    for j in range(0, n):
        print(matrix[i][j], end=' ')
    print()
