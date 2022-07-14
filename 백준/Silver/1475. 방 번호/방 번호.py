n = list(input())
nums = {str(i):0 for i in range(10)}

for i in n:
    if i == '6':
        nums['9'] += 1
    else:
        nums[i] += 1

nums['9'] += nums['6']
nums['6'] = 0

if nums['9'] % 2 == 0:
    nums['9'] //= 2
else:
    nums['9'] = nums['9'] // 2 + 1

print(max(nums.values()))