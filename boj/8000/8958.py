t = int(input())
result = []

for i in range(t):
    ox = input()
    result.append(ox)

for ox_list in result:
    score = 0
    continousScore = 0
    for ox in ox_list:
        if ox == 'O':
            if continousScore > 0:
                continousScore += 1
            else:
                continousScore = 1
            score += continousScore
        else:
            continousScore = 0
    print(score)
