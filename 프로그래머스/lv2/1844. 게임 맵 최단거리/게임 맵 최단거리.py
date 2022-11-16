from collections import deque

def solution(maps):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    x_len = len(maps)
    y_len = len(maps[0])
    
    visited = [[0]*y_len for _ in range(x_len)] 
    visited[0][0] = 1
    que = deque([(0, 0, 1)])
    while que:
        q = que.popleft()
        
        if q[0] == x_len-1 and q[1] == y_len-1:
            return q[2]
        
        for i in range(4):
            nx = q[1]+dx[i]
            ny = q[0]+dy[i]
            
            if -1<nx<y_len and -1<ny<x_len and visited[ny][nx]==0 and maps[ny][nx]==1:
                visited[ny][nx] = 1
                que.append((ny, nx, q[2]+1))
    
    return -1