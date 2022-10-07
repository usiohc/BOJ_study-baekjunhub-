from itertools import combinations as combi
def solution(nums):
    answer = 0
    
    for num in combi(nums, 3):
        if isprime(sum(num)):
            answer += 1
    
    return answer

def isprime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
        