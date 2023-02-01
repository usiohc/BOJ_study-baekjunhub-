def solution(n, stations, w):
    answer = 0
    
    cover = w*2 +1
    l = 1
    for s in stations:
        answer += (s-w-l) //cover
        if 0 < (s-w-l) %cover:
            answer += 1
        l = s+cover-w
    else:
        if l<=n:
            answer += (n-l+1)//cover
            if (n-l+1) % cover >0:
                answer += 1
    
    return answer