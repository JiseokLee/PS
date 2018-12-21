
age = input()
age = int(age)

birth_year = 2012 - age + 1

if(birth_year < 2000):
    birth_year = str(birth_year)
    print(int(birth_year[2:4]), 1)
else:
    birth_year = str(birth_year)
    print(int(birth_year[2:4]), 3)
