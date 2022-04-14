x = int(input())

temp = 1
while x > temp:
    x = x - temp
    temp += 1

if temp%2==0:
    a = x
    b = temp - a + 1
else:
    b = x
    a = temp - b + 1
print('{0}/{1}'.format(a, b))