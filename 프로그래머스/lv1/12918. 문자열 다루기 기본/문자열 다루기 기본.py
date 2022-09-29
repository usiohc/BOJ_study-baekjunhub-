def solution(s):
    return True if s.isnumeric() and len(s) in [4, 6] else False