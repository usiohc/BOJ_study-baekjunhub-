import sys

n, k = map(int, input().split())

nums = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
result = 0

for i in range(n-1, -1, -1):
    # print(k // nums[i], k)
    if k // nums[i] > 0:
        result += k//nums[i]
        k -= nums[i] * (k//nums[i])

print(result)