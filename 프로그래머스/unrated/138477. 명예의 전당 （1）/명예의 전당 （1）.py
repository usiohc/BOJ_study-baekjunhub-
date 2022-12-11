def solution(k, score):
    answer = []
    tmp = []
    for s in score:
        tmp.append(s)
        if len(tmp) > k:
            tmp.pop(tmp.index(min(tmp)))
        answer.append(min(tmp))
    return answer