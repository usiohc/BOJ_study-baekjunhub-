n = int(input())
f = int(input())
result = ( n//100) * 100
while result % f != 0:
    result += 1
print(str(result)[-2:])