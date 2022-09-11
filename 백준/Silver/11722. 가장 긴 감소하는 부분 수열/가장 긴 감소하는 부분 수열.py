n = int(input())
dp = [1] * n
array = list(map(int, input().split()))

for i in range(n):
    for j in range(i):
        if array[i] < array[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))