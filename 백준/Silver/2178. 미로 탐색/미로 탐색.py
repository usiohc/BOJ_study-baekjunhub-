from collections import deque

n, m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    queue = deque()
    # queue = deque((a, b))
    queue.append((a, b))
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if miro[nx][ny]==0:
                continue
            elif miro[nx][ny]==1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx, ny))

    return miro[n-1][m-1]

print(bfs(0, 0))