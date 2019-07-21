matrix = [[0]*27 for i in range(27)]
next_generation = [[0]*27 for i in range(27)]

for i in range(1, 26):
    input_list = list(map(int, input().split()))
    for j in range(0, 25):
        matrix[i][j+1] = input_list[j]

for i in range(1, 26):
    for j in range(1, 26):
        life = matrix[i-1][j-1] + matrix[i][j-1] + matrix[i+1][j-1] + matrix[i-1][j] + \
            matrix[i+1][j] + matrix[i-1][j+1] + \
            matrix[i][j+1] + matrix[i+1][j+1]
        if matrix[i][j] == 0:
            next_generation[i][j] = 1 if life == 3 else 0
        else:
            next_generation[i][j] = 1 if life == 2 or life == 3 else 0

for i in range(1, 26):
    for j in range(1, 26):
        print(next_generation[i][j], end=' ')
    print()
