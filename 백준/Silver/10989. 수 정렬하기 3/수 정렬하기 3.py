import sys

n = int(input())
nums = [0] * 10001

for i in range(n):
    temp = int(sys.stdin.readline())
    nums[temp] += 1

for i in range(1, len(nums)):
    for _ in range(nums[i]):
        print(i)