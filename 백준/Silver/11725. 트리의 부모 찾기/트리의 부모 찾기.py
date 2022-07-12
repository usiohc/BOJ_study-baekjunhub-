from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
nodes = [0] * (n+1)

for _ in range(n-1):
    a, b, = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)
while queue:
    q = queue.popleft()
    for i in graph[q]:
        if nodes[i] == 0:
            nodes[i] = q
            queue.append(i)


for i in range(2, n+1):
    print(nodes[i])