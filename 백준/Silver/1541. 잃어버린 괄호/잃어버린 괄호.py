tmp = input().split('-')
nums = []
for i in tmp:
    cnt = 0
    t = i.split('+')
    for j in t:
        cnt += int(j)
    nums.append(cnt)
num = nums[0]
for i in range(1, len(nums)):
    num -= nums[i]
print(num)