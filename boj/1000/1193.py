n=1
a=1
b=1
cnt = 0
x = int(input())
isEnd = False

while True:
    if(n % 2 == 1):
        a = n
        b = 1
    else:
        a = 1
        b = n
    
    for i in range(0, n):
        cnt += 1
        if(cnt == x):
            print(str(a) + '/' + str(b))
            isEnd = True
            break
        if(n % 2 == 1):
            a -= 1
            b += 1
        else:
            a += 1
            b -= 1
    
    if(isEnd == True):
        break

    n += 1
