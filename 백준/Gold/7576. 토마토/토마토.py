from collections import deque
import sys
input = sys.stdin.readline


def bfs(isone):
    queue = deque(isone)
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
isone = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            isone.append((i, j))


bfs(isone)

mintomato = 0
maxtomato = 0
for g in graph:
    if 0 in g:
        mintomato = -1
    maxtomato = max(maxtomato, max(g))

if mintomato == -1:
    print(-1)
else:
    print(maxtomato-1)