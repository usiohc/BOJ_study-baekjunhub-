n, m = map(int, input().split())
array = tuple(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start<=end:
    mid = (start + end) // 2
    length = sum(i-mid if i > mid else 0 for i in array)

    if length < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)