n = int(input())

xy_list = []
for i in range(n):
    xy = list(map(int, input().split()))
    xy_list.append(xy)
    
xy_list.sort()
for x, y in xy_list:
    print(x, y)