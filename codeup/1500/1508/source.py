n = int(input())
matrix = []

for i in range(1, n+1):
    tmp = [0] * i
    matrix.append(tmp)

for i in range(0, n):
    num = int(input())
    matrix[i][0] = num
    for j in range(1, len(matrix[i])):
        matrix[i][j] = matrix[i][j-1] - matrix[i-1][j-1]

for i in range(0, n):
    for j in range(0, len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()
