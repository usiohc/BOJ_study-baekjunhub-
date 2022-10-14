def solution(s):
    answer = [0, 0]
    while s != '1':
        l = len(s)
        s = '1'*s.count('1')
        answer[1] += l-len(s)        
        s = bin(len(s))[2:]
        answer[0] += 1
    return answer