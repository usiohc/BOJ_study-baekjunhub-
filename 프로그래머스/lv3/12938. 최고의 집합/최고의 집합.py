from itertools import combinations

def solution(n, s):
    answer = [s//n for _ in range(n)]
    lastnum = sum(answer)
    
    if s//n == 0:
            return [-1]
        
    for i in range(s%n):
        if lastnum == s:
            return sorted(answer)
        lastnum+=1
        answer[i] += 1
    else:
        return sorted(answer)