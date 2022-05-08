import sys

n = int(input())
nums = [int(sys.stdin.readline()) for _ in range(n)]
nums.sort()

print(round(sum(nums)/n))
print(nums[(n//2)])

nums_dic = {}
for i in nums:
    if i in nums_dic:
        nums_dic[i] += 1
    else:
        nums_dic[i] = 1


dic_max = max(nums_dic.values())
temp = []
for i in set(nums):
    if nums_dic[i] == dic_max:
        temp.append(i)
temp.sort()

if len(temp) > 1:
    print(temp[1])
else:
    print(temp[0])

print(max(nums)-min(nums))