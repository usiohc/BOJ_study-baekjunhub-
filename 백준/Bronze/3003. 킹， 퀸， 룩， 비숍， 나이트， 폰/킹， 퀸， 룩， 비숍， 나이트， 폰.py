cp = [1, 1, 2, 2, 2, 8]
tmp = list(map(int, input().split()))
for i in range(6):
    print(cp[i]-tmp[i], end=' ')