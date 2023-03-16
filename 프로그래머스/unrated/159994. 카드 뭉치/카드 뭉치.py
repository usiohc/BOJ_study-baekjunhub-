def solution(cards1, cards2, goal):
    answer = []
    i, j = 0, 0
    
    for _ in range(len(goal)):
        if i<len(cards1) and cards1[i] == goal[i+j]:
            answer.append(cards1[i])
            i+=1
        elif j<len(cards2) and cards2[j] == goal[i+j]:
            answer.append(cards2[j])
            j+=1
    
    if answer == goal:
        return 'Yes'
    else:
        return 'No'