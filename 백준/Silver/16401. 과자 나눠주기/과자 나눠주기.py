n, m = map(int, input().split())
array = list(map(int, input().split()))

start, end = 1, max(array)
result = 0

while start<=end:
    mid = (start+end)//2
    tmp = 0
    for i in range(m):
        tmp += array[i]//mid

    if tmp >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)