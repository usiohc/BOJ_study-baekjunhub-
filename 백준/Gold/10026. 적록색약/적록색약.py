import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    global cnt
    if visited[x][y] == 1:
        return False

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if nx<=-1 or nx>=n or ny<=-1 or ny>=n or visited == 1:
            continue

        if rgbs[nx][ny] == rgbs[x][y]:
            visited[x][y] = 1
            dfs(nx, ny)

    return True

n = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
rgbs = [list(map(str, input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            cnt += 1
        if rgbs[i][j] == 'G':
            rgbs[i][j] = 'R'

rgcnt = 0
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            rgcnt += 1
        
print(cnt, rgcnt)