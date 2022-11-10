from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for per_d in permutations(dungeons):
        k_tmp = k
        cnt = 0
        for d in per_d:
            if d[0] > k_tmp:
                break
            else:
                cnt += 1
                k_tmp -= d[1]
        answer = max(cnt, answer)
    return answer