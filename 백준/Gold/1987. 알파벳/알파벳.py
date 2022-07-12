import sys
input = sys.stdin.readline

r, c = map(int, input().split())
alphas = [list(input()) for _ in range(r)]
visited = [0] * (26)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
maxnum = 0

def dfs(x, y, cnt):
    global maxnum
    maxnum = max(cnt, maxnum)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < r and ny < c and nx >= 0 and ny >= 0 and visited[ord(alphas[nx][ny]) - 65] == 0:
            visited[ord(alphas[nx][ny]) - 65] = 1
            dfs(nx, ny, cnt+1)
            visited[ord(alphas[nx][ny]) - 65] = 0


visited[ord(alphas[0][0]) - 65] = 1
dfs(0, 0, 1)

print(maxnum)