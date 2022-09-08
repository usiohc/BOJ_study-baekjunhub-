n = int(input())
dp = [0] * n
array = list(map(int, input().split()))
dp[0] = array[0]

for i in range(1, n):
    for j in range(i-1, -1, -1):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j]+array[i])
        else:
            dp[i] = max(dp[i], array[i])
print(max(dp))