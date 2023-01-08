def top(n, s, e, m, answer):
    if n==1:
        answer.append([s, e])
        return answer
    else:
        top(n-1, s, m, e, answer)
        answer.append([s, e])
        top(n-1, m, e, s, answer)
        

def solution(n):
    answer = []
    
    top(n, 1, 3, 2, answer)
    
    
    
    return answer