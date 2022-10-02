def solution(sizes):
    answer = 0
    w, h = 0, 0
    for i in range(len(sizes)):
        a, b = max(sizes[i]), min(sizes[i])
        w, h = max(w, a), max(h, b)

    answer = w * h
    return answer