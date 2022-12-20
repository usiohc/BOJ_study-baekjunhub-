from collections import deque

def solution(queue1, queue2):
    answer = 0
    tmp = len(queue1) * 3
    
    que1 = deque(queue1)    
    que2 = deque(queue2)    
    s1 = sum(que1)
    s2 = sum(que2)
    
    if (s1+s2)%2 != 0:
        return -1
    
    
    while True:
        if s1 < s2:
            q = que2.popleft()
            que1.append(q)
            s1, s2= s1+q, s2-q
            
        elif s1 > s2:
            q = que1.popleft()
            que2.append(q)
            s1, s2= s1-q, s2+q
            
        elif s1 == s2:
            break
    
        if answer == tmp:
            answer = -1
            break
            
        answer += 1
        
    return answer