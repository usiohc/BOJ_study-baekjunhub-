n = int(input())
m = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
visited = [False]*(n+1)
result = 0

def dfs(v):
    global result

    visited[v] = True
    for i in range(1, n+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)
            result += 1

dfs(1)
print(result)