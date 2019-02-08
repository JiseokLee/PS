import math

v1, v2, v3 = map(int, input().split())

vaccine = math.gcd(math.gcd(v1, v2), v3)

print(vaccine)
