def solution(n, t, m, p):
    nums = '0123456789ABCDEF'
    answer = '0'
    for i in range(t*m):
        ans = ''
        num = i
        while num > 0:
            num, mod = divmod(num, n)
            ans += nums[mod]
        answer += ans[::-1]
    
    result = ''
    for i in range(p-1, len(answer), m):
        result += answer[i]
    
    return result[:t]