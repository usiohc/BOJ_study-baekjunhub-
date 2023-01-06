def solution(ingredient):
    answer = 0
    
    lst = []
    for l in ingredient:
        lst.append(l)
        if lst[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                lst.pop()
            
    return answer