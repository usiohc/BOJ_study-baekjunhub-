from collections import deque

def bfs(s, v, graph):
    que = deque([s])
    result = 1
    v[s] = 1
    while que:
        q = que.popleft()
        for i in graph[q]:
            if v[i] == 0:
                result += 1
                que.append(i)
                v[i] = 1
    
    return result
    
def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    for w in wires:
        graph[w[0]].append(w[1])
        graph[w[1]].append(w[0])
    
    for i, j in wires:
        visited = [0]*(n+1)
        visited[j] = 1
        answer = min(answer, abs(bfs(i, visited, graph) *2 - n))
    
    return answer