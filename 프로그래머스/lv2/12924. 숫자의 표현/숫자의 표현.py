def solution(n):
    answer = 0
    for i in range(1, n+1):
        if i>n: break
        elif n % i ==0:
            answer += 1
        n -= i
    # 15 1
    # 14 2
    # 12 3
    # 9 4
    # 5 5
    return answer