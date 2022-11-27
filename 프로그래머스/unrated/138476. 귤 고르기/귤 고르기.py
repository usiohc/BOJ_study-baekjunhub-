from collections import Counter

def solution(k, tangerine):
    # nums = sorted((tangerine.count(i) for i in set(tangerine)), reverse=True)
    
    nums = Counter(tangerine).most_common()

    cnt = 0
    for num in nums:
        k -= num[1]
        cnt += 1
        if k <= 0:
            return cnt
