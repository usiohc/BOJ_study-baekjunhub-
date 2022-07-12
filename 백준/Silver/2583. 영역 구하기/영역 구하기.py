import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m, k = map(int, input().split())
graph = [[1] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 0

def dfs(x, y):
    global cnt
    if visited[x][y] == 1 or graph[x][y] == 0:
        return False
    visited[x][y] = 1

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
            continue
        if graph[nx][ny] == 0:
            continue
        if graph[nx][ny] == 1 and visited[nx][ny] == 0:
            cnt += 1
            dfs(nx, ny)
    return True


nums = []
result = 0
for i in range(n):
    for j in range(m):
        cnt = 1
        if dfs(i, j):
            result +=1
            nums.append(cnt)

print(result)
print(*sorted(nums))