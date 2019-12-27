matrix = [[0]*11 for i in range(11)]

for i in range(1, 10):
    input_list = list(map(int, input().split()))
    for j in range(0, 9):
        matrix[i][j+1] = input_list[j]
r, c = map(int, input().split())

if matrix[r][c] == 1:
    print('-1')
else:
    mine = matrix[r-1][c-1] + matrix[r-1][c] + matrix[r-1][c+1] + \
        matrix[r][c-1] + matrix[r][c+1] + matrix[r+1][c-1] + \
        matrix[r+1][c] + matrix[r+1][c+1]
    print(mine)
