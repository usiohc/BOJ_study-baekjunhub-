def solution(k, d):
    answer = 0
    dd = d**2
    for n in range(0, d+1, k):
        answer += int(dd - n**2) **0.5 //k +1
    return answer