def solution(n):
    answer = 0
    cnt = (bin(n)[2:]).count('1')
    while answer == 0:
        n+=1
        if (bin(n)[2:]).count('1') == cnt:
            answer = n
    return answer