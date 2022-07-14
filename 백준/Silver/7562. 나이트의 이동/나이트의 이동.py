from collections import deque

def bfs(a, b, x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        q = queue.popleft()
        x, y = q

        if a==x and b==y:
            break
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<=-1 or nx>=l or ny<=-1 or ny>=l:
                continue

            if graph[nx][ny]==0:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))

dx = [-1, -2,-2,-1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2,-2,-1, 1, 2]
for _ in range(int(input())):
    l = int(input())
    graph = [[0] * l for _ in range(l)]
    a, b = map(int, input().split())
    x, y = map(int, input().split())
    graph[x][y] = 1
    
    bfs(a, b, x, y)
    print(graph[a][b]-1)