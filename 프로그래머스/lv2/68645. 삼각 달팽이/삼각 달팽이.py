def solution(n):
    answer = [[0]*n for _ in range(n)] 
    
    i = -1
    j = 0
    cnt = 1

    for d in range(n):
        for _ in range(d, n):
            if d % 3 == 0:
                i += 1
            elif d % 3 == 1:
                j += 1
            else:
                i -= 1
                j -= 1
            
            answer[i][j] = cnt
            cnt += 1
    
    ans = []
    for el in answer:
        for e in el:
            if e:
                ans.append(e)

    return ans