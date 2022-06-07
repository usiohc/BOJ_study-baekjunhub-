import sys
input = sys.stdin.readline

n = int(input())
grapes = [int(input()) for _ in range(n)]
dp = [0] * (n+1)
dp[0] = grapes[0]
if n>1:
    dp[1] = grapes[0]+grapes[1]
if n>2:
    dp[2] = max(grapes[2]+grapes[0], grapes[2]+grapes[1], dp[1])
for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-3] + grapes[i-1] + grapes[i], dp[i-2] + grapes[i])
print(max(dp))