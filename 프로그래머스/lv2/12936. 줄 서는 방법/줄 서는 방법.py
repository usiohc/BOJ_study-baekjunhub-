import math

def solution(n, k):
    nums = list(range(1, n+1))
    answer = []
    while n != 0:
        num = math.factorial(n-1)
        q, k = (k-1)//num, k%num
        answer.append(nums.pop(q))
        n -= 1
    return answer