n = int(input())
for i in range(n):
    OX = list(filter(str, input().split('X')))

    temp = 0
    for j in range(len(OX)) :
        temp += int(len(OX[j]) * (len(OX[j]) + 1) / 2)
    print(temp)