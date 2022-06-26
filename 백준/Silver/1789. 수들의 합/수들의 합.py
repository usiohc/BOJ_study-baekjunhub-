s = int(input())
result = 0
for i in range(1, s+1):
    if s-i < 0:
        break
    s -= i
    result = i
print(result)