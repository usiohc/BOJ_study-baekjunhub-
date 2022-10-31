from math import ceil

def solution(progresses, speeds):
    answer = []
    result = []
    for p, s in zip(progresses, speeds):
        day = ceil((100-p)/s)
        answer.append(day)
    
    cnt = 0
    for i in range(len(answer)):
        if answer[cnt] < answer[i]:
            result.append(i-cnt)
            cnt = i
    result.append(len(answer) - cnt)
    
    return result