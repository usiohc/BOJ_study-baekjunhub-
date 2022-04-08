ans = 0
num = int(input())
if num == 1000:
    num -= 1

for x in range(1, num + 1):
    units = x%10
    tens = x%100//10
    hundreds = x%1000//100

    if x < 100:
        ans += 1
    elif hundreds - tens == tens - units:
        ans += 1
print(ans)