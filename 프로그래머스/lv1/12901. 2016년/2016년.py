from datetime import date

def solution(a, b):
    answer = date(2016, a, b).strftime('%a')
    return answer.upper()