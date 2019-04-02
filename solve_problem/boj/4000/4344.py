c = int(input())
results = []

for i in range(c):
    input_score = list(map(int, input().split()))
    del input_score[0]
    average = sum(input_score) / len(input_score)
    above_average = 0

    for score in input_score:
        if score > average:
            above_average += 1

    results.append(float(above_average / len(input_score) * 100))

for result in results:
    print('{:.3f}'.format(result) + '%')
