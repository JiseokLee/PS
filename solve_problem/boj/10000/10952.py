results = []

while(True):
    num1, num2 = map(int, input().split())
    if num1 == num2 == 0:
        break
    results.append(num1 + num2)

for result in results:
    print(result)
