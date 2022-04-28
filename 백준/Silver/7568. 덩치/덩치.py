n = int(input())
xy_list = []
for _ in range(n):
    xy_list.append(list(map(int, input().split())))

for i in xy_list:
    count = 1
    for j in xy_list:
        if i[0] < j[0] and i[1] < j[1]:
            count += 1
    print(count, end=' ')
