
menu = [0, 400, 340, 170, 100, 70]
menu_number1, menu_number2 = input().split()
menu_number1 = int(menu_number1)
menu_number2 = int(menu_number2)

sum_of_calorie = menu[menu_number1] + menu[menu_number2]

if(sum_of_calorie > 500):
    print('angry')
else:
    print('no angry')
