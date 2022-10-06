def solution(nums):
    cnt = len(nums)//2
    result = len(set(nums))
    if cnt <= result:
        answer = cnt
    else:
        answer = result
    return answer