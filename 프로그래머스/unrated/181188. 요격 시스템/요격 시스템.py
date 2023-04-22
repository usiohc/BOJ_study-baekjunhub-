def solution(targets):
    answer = 0
    
    targets.sort(key = lambda x: (x[1], x[0]))
    now_loc = [0, 0]
    
    for i, j in targets:
        if now_loc[1] <= i:
            answer += 1
            now_loc = [i, j]
        else:
            now_loc = [i, now_loc[1]]

    return answer