n = int(input())
left_sugar = n % 5
cnt = int(n / 5)

if left_sugar == 0:
    print(cnt)
elif (left_sugar == 1) or (left_sugar == 3):
    print(cnt + 1)
elif left_sugar == 2:
    if cnt < 2:
        print(-1)
    else:
        print(cnt + 2)
elif left_sugar == 4:
    if cnt < 1:
        print(-1)
    else:
        print(cnt + 2)
