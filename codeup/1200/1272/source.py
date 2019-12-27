k, h = map(int, input().split())
sumMoney = 0


def getCurrentMoney(n):
    currentMoney = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            currentMoney = int(i / 2) * 10
        else:
            currentMoney = int(i / 2) + 1
    return currentMoney


sumMoney += getCurrentMoney(k)
sumMoney += getCurrentMoney(h)

print(sumMoney)
