from collections import deque

def bfs(x, y, v):
    queue = deque()
    queue.append((x,y, v))
    while queue:
        q = queue.popleft()
        x, y, v = q

        if x == n-1 and y == m-1:
            print(visited[x][y][v]+1)
            return

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
                continue

            if graph[nx][ny] == 1 and v == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))

            elif graph[nx][ny] == 0 and visited[nx][ny][v]==0:
                visited[nx][ny][v] = visited[x][y][v] +1
                queue.append((nx, ny, v))

    print(-1)
    return

dx=[-1,1,0,0]
dy=[0,0,-1,1]

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

bfs(0,0,0)