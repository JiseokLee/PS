
num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)

if(num1 % 2 == 0):
    if(num2 % 2 == 0):
        print('짝수+짝수=짝수')
    else:
        print('짝수+홀수=홀수')
else:
    if(num2 % 2 == 0):
        print('홀수+짝수=홀수')
    else:
        print('홀수+홀수=짝수')
