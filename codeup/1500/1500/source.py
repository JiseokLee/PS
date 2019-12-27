n, m = map(int, input().split())
matrix = []

for i in range(0, n):
    inputMatrix = list(map(int, input().split()))
    matrix.append(inputMatrix)

for i in range(0, n):
    for j in range(0, m):
        print(matrix[i][j], end=' ')
    print()
