from collections import deque 

def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    A,B = deque(A),deque(B)
    
    while A:
        if A[-1]<B[0]:
            B.popleft()
            A.pop()
            answer+=1
        else:
            A.pop()
        
    return answer