def solution(d, budget):
    answer = 0
    
    while True:
        if not d or min(d) > budget:
            break
            
        budget -= min(d)
        d.remove(min(d))
        answer += 1
        
    
    return answer