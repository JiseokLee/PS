k, n = map(int, input().split())
sun_shield = 0
matrix = []

for i in range(k):
    input_matrix = list(map(int, input().split()))
    matrix.append(input_matrix)

for i in range(0, k):
    for j in range(0, k):
        if (matrix[i][j] != -1) and (1 <= matrix[i][j]+n <= 5):
            sun_shield += 1

print(sun_shield)
