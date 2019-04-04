n = int(input())
first_num = n
cycle = 0

while True:
    cycle += 1
    calculated = int((n / 10)) + (n % 10)
    new_num = (n % 10) * 10 + (calculated % 10)

    if new_num == first_num:
        print(cycle)
        break
    else:
        n = new_num
