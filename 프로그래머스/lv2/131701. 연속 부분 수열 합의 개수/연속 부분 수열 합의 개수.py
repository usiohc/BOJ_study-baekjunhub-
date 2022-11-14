def solution(elements):
    answer = set()
    
    for l in range(1, len(elements)+1):
        for j in range(len(elements)):
            if j+l < len(elements)+1:
                answer.add(sum(elements[j:j+l]))
            else:
                answer.add(sum(elements[j:]+elements[:(j+l)%len(elements)]))
    
    return len(answer)