def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def dfs(nums, n):
    global cnt
    if is_prime(int(n)):
        cnt.add(int(n))
    
    for i in range(len(nums)):
        t_n = nums.pop(i)
        dfs(nums, n+t_n)
        nums.insert(i, t_n)

def solution(numbers):
    global cnt
    cnt = set()
    
    nums = list(map(str, numbers))
    for i in range(len(nums)):
        t_n = nums.pop(i)
        dfs(nums, t_n)
        nums.insert(i, t_n)
    
    return len(cnt)