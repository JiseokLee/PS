n = int(input())
matrix = [[0]*n for i in range(n)]
cnt = 1
row = n-1
col = 0
sw = False

for i in range(n, 0, -1):
    if sw == False:
        for j in range(0, i):
            matrix[row][col] = cnt
            if j == i-1:
                row += 1
                cnt += 1
                sw = True
            else:
                row -= 1
                col += 1
                cnt += 1
    else:
        for j in range(0, i):
            matrix[row][col] = cnt
            if j == i-1:
                col += 1
                cnt += 1
                sw = False
            else:
                row += 1
                col -= 1
                cnt += 1

for i in range(0, n):
    for j in range(0, n):
        print(matrix[i][j], end=' ')
    print()
