n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)

for i in range(n-1, -1, -1):
    if array[i][0] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(array[i][1] + dp[i+ array[i][0]], dp[i+1])

print(dp[0])