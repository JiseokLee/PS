num = int(input())
isPrime = 'prime'

for i in range(2, num):
    if num % i == 0:
        isPrime = 'not prime'
        break

print(isPrime)
