def solution(cookie):
    answer = 0
    max_ans = sum(cookie)//2
    
    m = 1
    while m < len(cookie):
        sum_l, sum_r = cookie[m-1], cookie[m]
        l, r = m-1, m
        
        while True:
            if sum_l == sum_r:
                answer = max(answer, sum_l)
                
            if sum_l <= sum_r and l-1 >= 0:
                l -= 1
                sum_l += cookie[l]
            elif sum_l >= sum_r and r+1 < len(cookie):
                r += 1
                sum_r += cookie[r]
            else:
                break
        
        if answer == max_ans:
            return answer
        m += 1


    return answer