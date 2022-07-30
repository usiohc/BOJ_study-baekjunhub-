import sys
input = sys.stdin.readline

k, n = map(int, input().split())
array = [int(input()) for _ in range(k)]

start, end = 1, max(array)
length = 0

while start<=end:
    mid = (start + end) // 2
    cnt = 0
    for i in array:
        cnt += i//mid

    if cnt < n:
        end = mid - 1
    else:
        length = mid
        start = mid + 1

print(length)