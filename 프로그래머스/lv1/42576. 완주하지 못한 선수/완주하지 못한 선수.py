def solution(participant, completion):
    hash_result = 0
    dic = {}
    for e in participant:
        dic[hash(e)] = e
        hash_result += hash(e)
    for e in completion:
        hash_result -= hash(e)
    
    return dic[hash_result]