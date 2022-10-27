def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key = len)
    for el in s:
        ss = el.split(',')
        for el2 in ss:
            if int(el2) not in answer:
                answer.append(int(el2))
    return answer