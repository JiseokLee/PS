matrix = []
isProblem = False

for i in range(10):
    board = list(map(int, input().split()))
    matrix.append(board)

horse = list(map(int, input().split()))

for i in range(0, 10):
    if horse[i] == 0:
        continue
    isProblem = False
    for j in range(9, -1, -1):
        if matrix[j][i] != 0:
            if matrix[j][i] > 0:
                print(i+1, 'crash')
                isProblem = True
                break
            else:
                print(i+1, 'fall')
                isProblem = True
                break
    if not isProblem:
        print(i+1, 'safe')
