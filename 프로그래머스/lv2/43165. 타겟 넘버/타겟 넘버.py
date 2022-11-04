def to_target(nums, n, idx):
    global tg, cnt
    
    if idx == len(nums):
        if tg == n:
            cnt += 1
        return
    
    to_target(nums, n+nums[idx], idx+1)
    to_target(nums, n-nums[idx], idx+1)

def solution(numbers, target):
    global tg, cnt
    cnt = 0
    tg = target
    
    to_target(numbers, 0, 0)
    return cnt