import copy
from collections import deque
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
nums = [graph[i][j] for j in range(n) for i in range(n)]
nums = sorted(list(set(nums)))


def bfs(i, j, num):
    queue = deque()
    queue.append((i,j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                continue
            if newgraph[nx][ny] > num:
                newgraph[nx][ny] = -1
                queue.append((nx, ny))

result = 0
for num in range(max(nums)+1):
    newgraph = copy.deepcopy(graph)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if newgraph[i][j] > num:
                bfs(i, j, num)
                cnt += 1
    result = max(result, cnt)

print(result)