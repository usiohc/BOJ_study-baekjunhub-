from itertools import combinations

def solution(number):
    answer = 0
    num_lst = list(combinations(number, 3))
    for n in num_lst:
        if sum(n) == 0:
            answer += 1
    return answer