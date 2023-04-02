def solution(scores):
    answer = 0
    
    ms0, ms1 = 1e6, 0

    ws0, ws1 = scores[0]
    ws = ws0+ws1
    for a, b in sorted(scores[1:], key=lambda x:(-x[0], x[1])):
        if ws0<a and ws1<b:
            return -1    
        
        if ms0>=a and ms1<=b:
            
            if ws < a+b:
                answer += 1        
            ms0, ms1 = a, b

    return answer+1