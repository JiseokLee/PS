x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
matrix = [[0]*7 for i in range(7)]

for i in range(0, 7):
    matrix[3][i] = 1

if x1 == 4:
    for i in range(0, 7):
        matrix[i][y1-1] = 1

if x2 == 4:
    for i in range(0, 7):
        matrix[i][y2-1] = 1

if x3 == 4:
    for i in range(0, 7):
        matrix[i][y3-1] = 1

for index in range(2):
    if matrix[x1-1][y1-1] == 1:
        for i in range(0, 7):
            matrix[x1-1][i] = 1
            matrix[i][y1-1] = 1

    if matrix[x2-1][y2-1] == 1:
        for i in range(0, 7):
            matrix[x2-1][i] = 1
            matrix[i][y2-1] = 1

    if matrix[x3-1][y3-1] == 1:
        for i in range(0, 7):
            matrix[x3-1][i] = 1
            matrix[i][y3-1] = 1

matrix[x1-1][y1-1] = 2
matrix[x2-1][y2-1] = 2
matrix[x3-1][y3-1] = 2

for i in range(0, 7):
    for j in range(0, 7):
        print(matrix[i][j], end=' ')
    print()
