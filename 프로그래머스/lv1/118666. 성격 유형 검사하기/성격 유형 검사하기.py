def solution(survey, choices):
    answer = ''
    personality_type = {ord('R')+ord('T'):{'R':0,'T':0},
                        ord('C')+ord('F'):{'C':0,'F':0},
                        ord('J')+ord('M'):{'J':0,'M':0},
                        ord('A')+ord('N'):{'A':0,'N':0}}

    for e, c in zip(survey, choices):
        c -= 4
        l,r = e[0], e[1]
        k = ord(l)+ord(r)
        if c<0:
            personality_type[k][l] -= c
        elif c>0:
            personality_type[k][r] += c
    
    for e in personality_type.values():
        answer += max(e, key=e.get)
    return answer