import sys
input = sys.stdin.readline

n, c = map(int, input().split())
nums = sorted([int(input()) for _ in range(n)])

start, end = 1, max(nums)-1
result = 0

while start<=end:
    mid = (start+end)//2
    cnt = 1
    tmp = nums[0] + mid

    for i in range(1, n):
        if tmp <= nums[i]:
            cnt += 1
            tmp = nums[i]+mid

    if cnt < c:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)