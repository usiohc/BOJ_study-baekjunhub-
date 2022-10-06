def isprime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    
    return True

def solution(n):
    answer = 0
    cnt = 1
    if n >= 3:
        cnt += 1
        
    for i in range(4, n+1):
        if isprime(i):
            cnt += 1
        
    
    return cnt