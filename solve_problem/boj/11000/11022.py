t = int(input())
results = []

for i in range(1, t+1):
    num1, num2 = map(int, input().split())
    results.append('Case #' + str(i) + ': ' + str(num1) +
                   ' + ' + str(num2) + ' = ' + str(num1+num2))

for result in results:
    print(result)
