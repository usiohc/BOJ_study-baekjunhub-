import sys 
input = sys.stdin.readline

n = int(input())

def solution(n):
    lines_dic = {}
    dp = [1 for _ in range(n)]
    for _ in range(n):
        A, B = map(int, input().split())
        lines_dic[A] = B
    lines = sorted(lines_dic.items())

    for i in range(1, n):
        for j in range(i):
            if lines[j][1] < lines[i][1]:
                dp[i] = max(dp[i], dp[j]+1)

    return n-max(dp)
            
print(solution(n))