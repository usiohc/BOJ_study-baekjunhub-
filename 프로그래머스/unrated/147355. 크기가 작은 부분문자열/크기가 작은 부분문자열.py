def solution(t, p):
    answer = 0
    lp = len(p)
    p = int(p)
    for i in range(len(t)-lp+1):
        if p >= int(t[i:i+lp]):
            answer += 1
    return answer