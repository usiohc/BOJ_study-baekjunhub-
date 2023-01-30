from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    
    answer = 0
    dp = [0] * (y+1)
    que = deque()
    que.append(x)
    while que:
        q = que.popleft()
        
        if 1 <= q+n <= y and dp[q+n] == 0:
            dp[q+n] = dp[q]+1
            que.append(q+n)
        if 1 <= q*2 <= y and dp[q*2] == 0:
            dp[q*2] = dp[q]+1
            que.append(q*2)
        if 1 <= q*3 <= y and dp[q*3] == 0:
            dp[q*3] = dp[q]+1
            que.append(q*3)
    
    if dp[y]:
        return dp[y]
    else:
        return -1