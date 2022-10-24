def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations), -1, -1):
        tmp = 0
        for ci in citations:
            if ci >= i:
                tmp+=1
            else:
                break
        
        if i <= tmp:
            answer = i
            break
    
    return answer