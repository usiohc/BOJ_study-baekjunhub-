def solution(s):
    answer = ''
    
    cnt = len(s)
    if cnt%2 == 0:
        answer = s[cnt//2-1:cnt//2+1]
    else:
        answer = s[cnt//2]
    
    
    
    return answer