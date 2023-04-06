def solution(sequence, k):
    answer = [1e6, 1e6]

    l, r = 0, 0
    m_l = 1e6
    
    num = sequence[0]
    
    while 0<=l<=r<len(sequence):
        if sequence[r] == k:
            return [r, r]
        
        if num == k:
            if r-l < m_l:
                m_l = r-l
                answer = [l, r]
            l += 1
            num -= sequence[l-1]
        elif num > k:
            l += 1
            num -= sequence[l-1]
        else:
            r += 1
            if r == len(sequence):
                break
            num += sequence[r]
        
        # print(l, r, num,'/', r-l, m_l)
    
    return answer