def isHanNumber(num):
    left = num // 100 % 10
    middle = num // 10 % 10
    right = num % 10
    if middle * 2 == left + right:
        return True
    return False


n = int(input())

if n < 100:
    print(n)
else:
    result = 99
    for i in range(100, n+1):
        if isHanNumber(i):
            result += 1
    if n == 1000:
        result -= 1
    print(result)
