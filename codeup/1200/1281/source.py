a, b = map(int, input().split())
result = 0

for i in range(a, b+1):
    if i % 2 == 0:
        print('-' + str(i), end='')
        result -= i
    else:
        if i == a:
            print(str(i), end='')
        else:
            print('+' + str(i), end='')
        result += i

if result > 0:
    print('=+' + str(result))
else:
    print('=' + str(result))
