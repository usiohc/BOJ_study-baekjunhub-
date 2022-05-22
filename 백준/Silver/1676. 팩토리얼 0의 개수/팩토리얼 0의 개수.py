import math

n = str(math.factorial(int(input())))

result = 0
temp = 0
while True:
    temp -= 1
    if n[temp] == '0':
        result += 1
    else: break

print(result)