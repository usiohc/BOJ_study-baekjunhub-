n, l = map(int, input().split())
array = sorted(list(map(int, input().split())))
cnt = 0
idx = 0
for i in range(n):
    if idx < array[i]:
        idx = array[i]+l-1
        cnt += 1

print(cnt)