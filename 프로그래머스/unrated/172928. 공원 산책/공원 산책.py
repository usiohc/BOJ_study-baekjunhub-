dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solution(park, routes):
    answer = []
    ly, lx = len(park), len(park[0])
    
    x, y = 0, 0
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                x, y = j, i
                break
        else:
            continue
        break
    
    
    for r in routes:
        c, d = r.split()
        nx, ny = x, y
        tmp_c = 0
        for _ in range(int(d)):
            if c == 'E':
                nx, ny = nx+dx[0], ny+dy[0]    
            elif c == 'W':
                nx, ny = nx+dx[1], ny+dy[1]    
            elif c == 'S':
                nx, ny = nx+dx[2], ny+dy[2]    
            elif c == 'N':
                nx, ny = nx+dx[3], ny+dy[3]    
            
            if 0>nx or nx>=lx or 0>ny or ny>=ly or park[ny][nx] == 'X':
                nx, ny = x, y
                break
        x, y = nx, ny
        
    return [y, x]