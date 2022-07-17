n = int(input())
nums = {}
result = []
for _ in range(n):
    tmp = input()
    if tmp in nums:
        nums[tmp] += 1
    else:
        nums.setdefault(tmp, 1)

tmp = max(nums.values())
for k, v in nums.items():
    if tmp == v:
        result.append(int(k))
result.sort()

print(result[0])