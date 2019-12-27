a = int(input())
b = int(input())
variabilities = list(map(int, input().split()))
final_money = a

for variability in variabilities:
    if variability < 0:
        final_money = final_money - (final_money * (variability * -1 / 100))
    else:
        final_money = final_money + (final_money * (variability / 100))

print(round(final_money - a))
if(final_money - a == 0):
    print('same')
elif(final_money - a < 0):
    print('bad')
else:
    print('good')
