import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = [int(input()) for _ in range(m)]

start, end = 1, max(array)
result = 10 ** 9 + 1

while start <= end:
    mid = (start+end) // 2
    cnt = 0


    for i in range(m):
        if array[i] % mid == 0:
            cnt += array[i] // mid
        else:
            cnt += array[i] // mid + 1

        if cnt > n:
            break

    if cnt > n:
        start = mid + 1
    else:
        result = min(result, mid)
        end = mid - 1

print(result)