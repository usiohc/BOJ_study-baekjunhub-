from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(maps):
    global n, m
    answer = 0
    m, n = len(maps), len(maps[0])
    maps = [list(t) for t in maps]
    
    s, e, l = tuple(), tuple(), tuple()
    for i in range(m):
        for j in range(n):
            cmd = maps[i][j]
            if cmd == 'S':
                s = (i, j, 0)
            elif cmd == 'E':
                e = (i, j, 0)
            elif cmd == 'L':
                l = (i, j, 0)    
    
    def bfs(start, end, maps):
        visited = [[False]*n for _ in range(m)]
        que = deque()
        que.append(start)
        visited[start[0]][start[1]] = True
        while que:
            x, y, c = que.popleft()
            
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                
                if nx<=-1 or nx>=m or ny<=-1 or ny>=n:
                    continue
                if visited[nx][ny] or maps[nx][ny] =='X':
                    continue
                
                if nx == end[0] and ny == end[1]:
                    return c+1
                que.append((nx, ny, c+1))
                visited[nx][ny] = True
        return -1

    stol = bfs(s, l, maps)
    ltoe = bfs(l, e, maps)
    
    if stol>0 and ltoe>0:
        return stol+ltoe
    else:
        return -1
