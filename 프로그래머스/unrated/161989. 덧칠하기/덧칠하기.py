def solution(n, m, section):
    answer = 1
    num = section[0]
    m -= 1
    for i in range(1, len(section)):
        if section[i-1] + m >= section[i] and num+m>= section[i]:
            continue
        num = section[i]
        answer += 1

    
    return answer