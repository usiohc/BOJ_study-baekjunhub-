input()
nums = sorted(list(map(int, input().split())))
x = int(input())

l, r = 0, len(nums)-1
cnt = 0
while l < r:
    result = nums[l] + nums[r]
    if result == x:
        cnt += 1
        l += 1
    elif result < x:
        l += 1
    elif result > x:
        r -= 1

print(cnt)