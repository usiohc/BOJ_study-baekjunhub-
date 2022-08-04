n, m = map(int, input().split())
array = list(map(int, input().split()))

start, end = max(array), sum(array)

result = 100000 * 10000
while start<=end:
    mid = (start + end) // 2
    cnt = 1
    length = 0

    for i in range(n):
        if length+array[i] <= mid:
            length += array[i]
        else:
            length = array[i]
            cnt += 1
            if cnt > m:
                break

    if cnt > m:
        start = mid + 1
    else:
        end = mid-1
        if mid >= start:
            result = min(result, mid)

print(result)