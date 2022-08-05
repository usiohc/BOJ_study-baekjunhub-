import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = [int(input()) for _ in range(n)]

start, end = min(array), sum(array)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = mid
    cnt = 1

    for i in range(n):
        if total - array[i] < 0:
            total = mid
            cnt += 1
        total -= array[i]

    if cnt > m or mid < max(array):
        start = mid + 1
    else:
        end = mid - 1
        result = mid

print(result)