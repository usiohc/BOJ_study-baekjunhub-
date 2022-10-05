from itertools import permutations

def solution(numbers):
    answer = sorted(list(set(map(sum, permutations(numbers, 2)))))
    return answer