def solution(participant, completion):
    hash_result = 0
    dic = {}
    for e in participant:
        dic[e] = dic.get(e, 0) +1
    for e in completion:
        dic[e] -= 1
    
    answer = [k for k, v in dic.items() if v > 0]
    
    return answer[-1]