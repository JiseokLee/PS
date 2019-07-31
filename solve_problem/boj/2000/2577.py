num1 = int(input())
num2 = int(input())
num3 = int(input())
result = str(num1 * num2 * num3)
number_list = []

for i in range(0, 10):
    count = 0
    for num in result:
        if str(i) == num:
            count += 1
    number_list.append(count)

for item in number_list:
    print(item)
