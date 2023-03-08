def solution(n, works):
    
    dp = [0] * (max(works)+1)
    for w in works:
        dp[w] += 1

    idx_works = []
    for i in range(len(dp)-1, 0, -1):
        if dp[i] > 0 and n>0:
            if dp[i]-n >= 0:
                dp[i-1] += n
                dp[i] -= n
                n = 0
            else:
                dp[i-1] += dp[i]
                n -= dp[i]
                dp[i] = 0
            
        if dp[i] > 0 and n == 0:
            idx_works.append((i, dp[i]))
    
    num = 0
    if idx_works:
        for x, i in idx_works:
            for _ in range(i):
                num += x**2
        return num
    else:
        return 0
