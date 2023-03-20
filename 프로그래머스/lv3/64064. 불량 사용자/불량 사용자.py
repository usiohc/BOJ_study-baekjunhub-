from itertools import product
import re

def solution(user_id, banned_id):
    answer = set()
    set_id = [set() for _ in range(len(banned_id))]
    
    for i in range(len(banned_id)):
        bi = banned_id[i]
        bil = len(bi)
        pattern = ''
        for b in bi:
            if b == '*':
                pattern += '.'
            else:
                pattern += b
        
        for ui in user_id:
            if bil == len(ui) and re.match(pattern, ui):
                set_id[i].add(ui)
    # print(set_id)
    
    for si in list(product(*set_id)):
        if len(set(si)) == len(si):
            answer.add(tuple(sorted(si)))
    # print(answer)
    
    return len(answer)