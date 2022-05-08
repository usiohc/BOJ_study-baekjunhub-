import sys
n = int(input())
nums = [int(sys.stdin.readline()) for _ in range(n)]
nums.sort()

for i in range(n):
    print(nums[i])