def solution(m, n, sx, sy, balls):
    answer = []
    
    for bx, by in balls:
        xys = []
        if sy == by:
            if sx>bx:
                xys.append((2 * m - sx - bx) **2)
            else:
                xys.append((sx + bx)**2)
                
            xys.append((bx - sx) **2 + 4 * sy ** 2)
            xys.append((bx - sx) **2 + 4 * (n - sy)**2)
        elif sx == bx:
            if sy>by:
                xys.append((2 * n - sy - by) **2)
            else:
                xys.append((sy + by)**2)
                
            xys.append((by - sy) **2 + 4 * sx ** 2)
            xys.append((by - sy) **2 + 4 * (m - sx)**2)
        else:
            xys.append((bx - sx)**2 + (by + sy)**2)
            xys.append((bx + sx)**2 + (by - sy)**2)
            xys.append((by - sy)**2 + (2 * m - sx - bx)**2)
            xys.append((bx - sx)**2 + (2 * n - sy - by)**2)
            
        answer.append(min(xys))
    return answer


