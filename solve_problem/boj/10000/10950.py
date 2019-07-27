t = int(input())
results = []

for i in range(t):
    num1, num2 = map(int, input().split())
    results.append(num1 + num2)

for num in results:
    print(num)
