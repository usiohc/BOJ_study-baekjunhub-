def solution(a, b):
    answer = sum(map(lambda x: a[x]*b[x], range(len(a))))

    return answer