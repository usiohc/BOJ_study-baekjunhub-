import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(v):
    visited[v] = True
    for i in range(1, n+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)


n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
visited = [False] * (n+1)
cnt = 0

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)