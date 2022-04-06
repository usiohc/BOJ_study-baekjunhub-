a = int(input())
b = int(input())
c = int(input())
result = str(a * b * c)

for i in range(10):
    temp = 0
    for j in range(len(result)):
        if str(i) == result[j]:
            temp += 1
    print(temp)