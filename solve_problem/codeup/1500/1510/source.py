def increse_row(row, col, n):
    if row == n-1:
        row = 0
    else:
        row += 1

    return row, col


def next_row_col(row, col, n):
    if row == 0:
        row = n-1
    else:
        row -= 1

    if col == n-1:
        col = 0
    else:
        col += 1

    return row, col


n = int(input())
matrix = [[0]*n for i in range(n)]
row = 0
col = int(n/2)

matrix[row][col] = 1

for i in range(2, n**2+1):
    if (i-1) % n == 0:
        row, col = increse_row(row, col, n)
        matrix[row][col] = i
    else:
        row, col = next_row_col(row, col, n)
        matrix[row][col] = i

for i in range(0, n):
    for j in range(0, n):
        print(matrix[i][j], end=' ')
    print()
