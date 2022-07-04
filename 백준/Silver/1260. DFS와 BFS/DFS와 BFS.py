import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1
# print(graph)


def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in range(1, n+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        q = queue.popleft()
        print(q, end=' ')
        for i in range(1, n+1):
            if not visited[i] and graph[q][i] == 1:
                queue.append(i)
                visited[i] = True

visited = [False] * (n+1)
dfs(v)
print()

visited = [False] * (n+1)
bfs(v)