def solution(dirs):
    answer = set()
    
    # U=0 R=1 D=2 L=3
    dx = [0, 1, 0,-1]
    dy = [1, 0,-1, 0]
    
    x1, y1 = 0, 0
    
    for d in dirs:
        x2, y2 = x1, y1
        
        if d == 'U':
            x2 += dx[0]
            y2 += dy[0]
        elif d == 'R':
            x2 += dx[1]
            y2 += dy[1]
        elif d == 'D':
            x2 += dx[2]
            y2 += dy[2]
        elif d == 'L':
            x2 += dx[3]
            y2 += dy[3]

        if -5<=x2<=5 and -5<=y2<=5:
            answer.add((x1,y1,x2,y2))
            answer.add((x2,y2,x1,y1))
            x1, y1 = x2, y2
        
    return len(answer)//2