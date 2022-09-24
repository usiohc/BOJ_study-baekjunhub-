def sumstr(x):
    return sum(map(int, str(x)))
def solution(x):
    answer = True
    if x % sumstr(x) != 0:
        answer = False
    return answer