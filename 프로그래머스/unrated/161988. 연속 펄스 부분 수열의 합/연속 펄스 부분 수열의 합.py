def solution(s):
    answer = 0

    pulse1 = 0
    pulse2 = 0
    
    for i in range(len(s)-1, -1, -1):
        if i%2 == 0:
            pulse1 = max(pulse1+ s[i], s[i])
            pulse2 = max(pulse2+ -s[i], -s[i])
        else:
            pulse1 = max(pulse1+ -s[i], -s[i])
            pulse2 = max(pulse2+ s[i], s[i])

        answer = max(pulse1, pulse2, answer)
            
    return answer