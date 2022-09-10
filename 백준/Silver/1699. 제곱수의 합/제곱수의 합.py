n = int(input())
dp = [0] * (n+1)
squared = [i**2 for i in range(1, n+1)]

for i in range(1, n+1):
    tmp = []
    for j in squared:
        if j > i:
            break
        tmp.append(dp[i-j])
    dp[i] = min(tmp) + 1

print(dp[n])