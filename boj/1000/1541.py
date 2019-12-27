exp = input().split('-')
itemList = []

for t in exp:
    temp = list(map(int, t.split('+')))
    itemList.append(sum(temp))

total = itemList[0]

for item in itemList[1:]:
    total -= item

print(total)
