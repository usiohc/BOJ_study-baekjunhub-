def solution(routes):
    answer = 0
    routes.sort(key = lambda x:(x[0], -x[1]))
    num = -30001
    print(routes)
    for l, r in routes:
        if l > num:
            answer += 1
            num = r
        else:
            num = min(num, r)
    return answer

