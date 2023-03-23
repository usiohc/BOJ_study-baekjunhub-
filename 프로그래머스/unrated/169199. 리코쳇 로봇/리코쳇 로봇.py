from collections import deque 

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def solution(b):
    board = [list(bb) for bb in b]
    # print(*board, sep='\n')
    
    ly, lx = len(board), len(board[-1])
    visited = [[0] * lx for _ in range(ly)]

    que = deque()
    for i in range(ly):
        for j in range(lx):
            if board[i][j] == 'R':
                que.append((i,j))
                break
        else:
            continue
        break
    
    while que:
        x, y = que.popleft()
    
        for i in range(4):
            nx, ny = x, y
            
            while -1<nx<ly and -1<ny<lx and board[nx][ny] != 'D':
                nx, ny = nx+dx[i], ny+dy[i]
            nx, ny = nx-dx[i], ny-dy[i]
            if x == nx and y == ny:
                continue

            if visited[nx][ny] != 0 and visited[nx][ny] < visited[x][y]+1:
                continue
            visited[nx][ny] = visited[x][y] + 1
            
            if board[nx][ny] == 'G':
                return visited[nx][ny]
            
            que.append((nx, ny))

    return -1