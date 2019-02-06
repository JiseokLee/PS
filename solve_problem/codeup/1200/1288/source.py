n, r = map(int, input().split())


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(int(factorial(n) / (factorial(r) * factorial(n-r))))
