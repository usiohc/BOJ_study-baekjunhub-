import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
start, end = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

m = int(input())
for _ in range(m):
    a, b, = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
def dfs(s, cnt):
    global result
    if s == end:
        result = cnt
    for i in graph[s]:
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt+1)

dfs(start, 0)

if result == 0:
    print(-1)
else:
    print(result)