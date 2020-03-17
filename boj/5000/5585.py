change = 1000 - int(input())
kindsOfMoney = [500, 100, 50, 10, 5, 1]
cnt = 0

while change != 0:
    for money in kindsOfMoney:
        if change // money > 0:
            cnt += change // money
            change = change % money

print(cnt)