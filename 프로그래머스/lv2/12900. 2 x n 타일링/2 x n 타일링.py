def solution(n):
    answer = 0
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 2
    dp[2] = 3
    
    for i in range(3, n+1):
        dp[i] = (dp[i-2]+dp[i-1]) % 1000000007
    
    return dp[n-1] % 1000000007