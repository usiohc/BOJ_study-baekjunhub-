from collections import defaultdict, deque

def solution(N, road, K):
    d = defaultdict(list)
    for a, b, c in road:
        d[a].append((b,c))
        d[b].append((a,c))

    visited = [0 for _ in range(N+1)]
    que = deque([(1, 0)])
    visited[0] = 1
    visited[1] = 1
    while que:
        a, t = que.popleft()
        
        for x, y in d[a]:
            if t + y <= K and (not visited[x] or t + y <= visited[x]):
                que.append((x, t + y))
                visited[x] = t + y
                
    answer = N - visited.count(0)
    return answer