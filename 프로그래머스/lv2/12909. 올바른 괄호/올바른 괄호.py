def solution(s):
    answer = True
    cnt = 0
    for el in s:
        if el == '(':
            cnt+=1
        else:
            cnt-=1
        
        if cnt < 0:
            answer = False
            break
    
    if cnt > 0:
        answer = False
    return answer