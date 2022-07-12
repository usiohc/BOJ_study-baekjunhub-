from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = [list(list(map(int, input().split())) for _ in range(n)) for _ in range(h)]

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dh = [0,0,0,0,-1,1]


def bfs():
    queue = deque(tomatos)

    while queue:
        que = queue.popleft()
        he, x, y = que
        for i in range(6):
            nh, nx, ny = he+dh[i], x+dx[i], y+dy[i]
            if nh<=-1 or nh>=h or nx<=-1 or nx>=n or ny<=-1 or ny>=m:
                continue

            if graph[nh][nx][ny] == 0:
                graph[nh][nx][ny] = graph[he][x][y] + 1
                queue.append((nh, nx, ny))


tomatos = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                tomatos.append((i,j,k))
bfs()

maxday = 0
flag = True
for i in range(h):
    for j in range(n):
        maxday = max(maxday, *graph[i][j])
        for k in range(m):
            if graph[i][j][k] == 0:
                flag = False

if flag:
    print(maxday-1)
else:
    print(-1)
