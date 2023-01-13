def solution(cards):
    answer = []
    visited = [0] * len(cards)
    
    for i in range(len(cards)):
        if visited[i] == 0:
            cnt = 1
            j = cards[i]-1
            visited[i] = 1
            while visited[j] == 0:
                visited[j] = 1
                cnt += 1
                j = cards[j]-1
            answer.append(cnt)
    
    if len(answer) == 1:
        return 0
    else:
        answer.sort()
        return answer[-2]*answer[-1]