from collections import Counter

def solution(want, number, discount):
    lst_want = []
    cnt = 0
    
    for w, i in zip(want, number):
        for j in range(i):
            lst_want.append(w)
    
    lst_want = Counter(lst_want)
    for i in range(10, len(discount)+1):
        if lst_want == Counter(discount[i-10:i]):
            cnt += 1
    
    return cnt if cnt > 0 else 0
