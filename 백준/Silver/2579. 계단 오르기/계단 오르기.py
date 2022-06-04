import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input().rstrip()) for _ in range(n)]
dp = []
dp.append(nums[0])
if n > 1:
    dp.append(max(dp[0]+nums[1], nums[1]))
if n > 2:
    dp.append(max(dp[0]+nums[2], nums[1]+nums[2]))

for i in range(3, n):
    dp.append(max(nums[i] + nums[i-1] + dp[i-3], nums[i] + dp[i-2]))

print(dp[-1])