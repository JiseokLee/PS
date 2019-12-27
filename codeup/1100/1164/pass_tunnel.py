
height_1, height_2, height_3 = input().split()
height_1 = int(height_1)
height_2 = int(height_2)
height_3 = int(height_3)

if(height_1 <= 170):
    print('CRASH')
elif(height_2 <= 170):
    print('CRASH')
elif(height_3 <= 170):
    print('CRASH')
else:
    print('PASS')
